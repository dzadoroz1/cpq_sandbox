from Scripting import SqlDbType

def process_active_rule(product,active_rule, selected_values):
    if not active_rule:
        return

    active_part_number = active_rule.PartNumber
    active_attr_name = selected_values.get(active_part_number)
    active_quantity = int(active_rule.DefaultQty)
    active_override = active_rule.Override

    if active_attr_name:
        active_attribute = product.AttrValue(active_attr_name, active_part_number)
        if active_override == 1 and active_attribute.Quantity != active_quantity:
            active_attribute.Quantity = active_quantity
        elif active_override == 0 and active_attribute.DefaultQuantity != active_quantity:
            active_attribute.DefaultQuantity = active_quantity
            active_attribute.Quantity = active_quantity

def update_attribute_quantities(product):
    selected_values = {str(values.ValueCode): attr.Name for attr in product.Attributes for values in attr.SelectedValues}

    if not selected_values:
        return

    value_codes = list(selected_values.keys())
    all_rules = []
    offset = 0
    fetch_size = 1000

    while True:
        sql_query = """
            SELECT Condition, PartNumber, DefaultQty, Override
            FROM DefaultQuantity
            WHERE TractionUnit = @traction_unit
            AND PartNumber IN ({})
            ORDER BY PartNumber
            OFFSET @offset ROWS FETCH NEXT @fetch_size ROWS ONLY
        """.format(", ".join(["@p{}".format(i) for i in range(len(value_codes))]))

        params = [SqlHelper.CreateParameter(product.PartNumber, "@traction_unit", SqlDbType.NVarChar)]
        params.extend(SqlHelper.CreateParameter(vc, "@p{}".format(i), SqlDbType.NVarChar) for i, vc in enumerate(value_codes))
        params.append(SqlHelper.CreateParameter(offset, "@offset", SqlDbType.Int))
        params.append(SqlHelper.CreateParameter(fetch_size, "@fetch_size", SqlDbType.Int))

        rules = SqlHelper.GetList(sql_query, *params)

        if not rules:
            break
        all_rules.extend(rules)

        if len(rules) < fetch_size:
            break

        offset += fetch_size

    if not all_rules:
        return

    current_pn = all_rules[0].PartNumber
    active_rule = None

    for rule in all_rules:
        condition = rule.Condition.strip() if rule.Condition else ""
        part_number = rule.PartNumber.strip()
        quantity_from_db = int(rule.DefaultQty)
        override_flag = int(rule.Override)

        if part_number != current_pn:
            process_active_rule(product, active_rule, selected_values)
            current_pn = rule.PartNumber
            active_rule = None

        if condition in ["", None] or condition in selected_values:
            if active_rule is None:
                active_rule = rule
            elif (active_rule.Condition in ["", None] and condition not in ["", None]) or (
                condition not in ["", None] and override_flag == 1 and active_rule.Override == 0
            ):
                active_rule = rule

    process_active_rule(product, active_rule, selected_values)

def update_attribute_default_quantities(product):
    sql_query = """
    SELECT PartNumber, DefaultQty
    FROM DefaultQuantity
    WHERE TractionUnit = @part_number AND (Condition = '' OR Condition IS NULL)
    """
    rules = SqlHelper.GetList(sql_query, SqlHelper.CreateParameter(product.PartNumber, "@part_number", SqlDbType.NVarChar))

    part_number_to_qty = {rule.PartNumber.strip(): int(rule.DefaultQty) for rule in rules}

    for item in product.Attributes:
        for attri in item.Values:
            if attri.ValueCode in part_number_to_qty:
                attri.DefaultQuantity = part_number_to_qty[attri.ValueCode]