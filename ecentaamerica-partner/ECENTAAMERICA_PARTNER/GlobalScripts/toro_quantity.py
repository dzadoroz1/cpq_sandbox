from Scripting import SqlDbType

def update_attribute_quantities(model_name, Product):
    sql_query = """
    SELECT attribute, attribute_value, condition, condition_attribute, quantity
    FROM TORO_QUANTITY_RULES
    WHERE model = @model_name
    """
    rules = SqlHelper.GetList(sql_query, SqlHelper.CreateParameter(model_name, "@model_name", SqlDbType.NVarChar))

    available_attributes = [[attr.Name, attr] for attr in Product.Attributes]
    target_attr_rules = [
        [
            rule.attribute.strip(),
            rule.attribute_value.strip(),
            int(rule.quantity),
            [(attr.strip(), cond.strip()) for attr, cond in zip(rule.condition_attribute.split("+"), rule.condition.split("+"))]
        ]
        for rule in rules
    ]

    for attribute_name, attribute_value, quantity, rules_list in target_attr_rules:
        target_attr = next((attr for name, attr in available_attributes if name == attribute_name), None)
        if not target_attr:
            continue
        condition_results = all(
            any(name == attr and any(selected.ValueCode == cond for selected in attr_obj.SelectedValues)
                for name, attr_obj in available_attributes)
            for attr, cond in rules_list
        )
        if condition_results:
            for item in target_attr.SelectedValues:
                if (attribute_value == "0" or item.ValueCode == attribute_value) and (item.Quantity == 1 and item.Quantity != quantity):
                    item.Quantity = quantity