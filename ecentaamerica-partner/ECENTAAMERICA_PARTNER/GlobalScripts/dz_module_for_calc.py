def count_ext(item, cf):
    '''
        Calculates extended price by multiplying price with quantity
        Formula: quantity * methodPrice
        param IQuoteItem item: item from quote Items collection
        param string cf: needed custom field name as string
		return: float
    '''
    quantity = item.Quantity
    customField = item.GetCustomField(cf)
    if quantity and customField.Value:
        return quantity * customField.Value


def copyDown(quote_items, cf):
    '''
        Copies % of MSRP from Main Item to its discountable line items
        param Quote2Context context: context for current quote
        param string cf: needed custom field name as string
        return: void
    '''
    main_item = None
    for item in quote_items:
        if item.IsLineItem:
            continue
        main_item = item.AsMainItem
        for child in main_item.GetChildItems():
            if not child["DZ_Discountable"]:
                continue
            child[cf] = main_item[cf]


def get_DZ_CUSTOM_PRICE_LIST(quote_items):
    '''
        Gets a list from DZ_CUSTOM_PRICE_LIST custom table, and makes it a dict with Part_number as key, and sql table row as object
        param Quote2Context context: context for current quote
		return: dict
    '''
    part_num_list = [item.PartNumber for item in quote_items]
    if not part_num_list:
        return {}
    part_nums_str = "', '".join(part_num_list)
    sql_query = '''SELECT MSRP, DNET, Part_number, Discountable
                   FROM DZ_CUSTOM_PRICE_LIST 
                   WHERE Part_number IN ('{}')'''.format(part_nums_str)
    prices = SqlHelper.GetList(sql_query)
    return {p.Part_number: p for p in prices}