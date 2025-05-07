from Scripting import SqlDbType, ISqlParameter

def pull_table_data(distributor, contract, items):
    added_items = [
        SqlHelper.CreateParameter(contract, "@contract", SqlDbType.NVarChar),
        SqlHelper.CreateParameter(distributor, "@distributor", SqlDbType.NVarChar)
    ]
    param_keys = []
    for idx, item in enumerate(items):
        key = "@sku_{}".format(idx)
        added_items.append(SqlHelper.CreateParameter(item.PartNumber, key, SqlDbType.NVarChar))
        param_keys.append(key)
    
    sql = """
    SELECT SKU, Discount, Rebate, tpc.Tier
    FROM TORO_PRICECONTRACT tpc
        INNER JOIN Toro_Tiers tt ON tpc.Tier = tt.Tier
    WHERE SKU IN ({skus}) 
        AND Contract = @contract
        AND Distributor = @distributor
    """.format(skus=",".join(key for key in param_keys))

    query = SqlHelper.GetList(sql, Array[ISqlParameter](added_items))
    return {row.SKU: row for row in query}

def calculate_award_price(contract_discount, msrp):
    return msrp * (1 - contract_discount / 100) if msrp > 0 else msrp

def calculate_rebate_amount(award_price, rebate_percent):
    award_price = award_price or 0.0
    rebate_percent = rebate_percent or 0.0
    return award_price * (rebate_percent / 100)

def calculate_percent(amount, total_amount):
    amount = amount or 0.0
    total_amount = total_amount or 0.0
    return (amount / total_amount) * 100 if total_amount != 0 else 0

def calculate_gross_amount(award_price, dealer_price, rebate_amount):
    award_price = award_price or 0.0
    dealer_price = dealer_price or 0.0
    rebate_amount = rebate_amount or 0.0
    return award_price - dealer_price + rebate_amount

def read_delta(item, field_name):
    try:
        return item.GetDelta(field_name)
    except SystemError as e:
        return 0.0

def roll_up_amounts(root_item, current_item, *field_names):
    for field_name in field_names:
        if root_item[field_name] is None:
            root_item[field_name] = 0.0
        
        delta = read_delta(current_item, field_name)
        if not delta and current_item[field_name]:
            root_item[field_name] += current_item[field_name]
        else:
            root_item[field_name] += delta

def generate_subtotal_template(*field_names):
    return {field_name: 0 for field_name in field_names}

def resolve_subtotal_none(subtotal, field_name):
    if subtotal[field_name] is None:
        subtotal[field_name] = 0.0