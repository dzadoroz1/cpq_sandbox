def count_ext(item, cf):
    '''
        Calculates extended price by multiplying price with quantity
        Formula: quantity * methodPrice
        param IQuoteItem item: item from quote Items collection
        param string cf: needed custom field name as string
    '''
    quantity = item.Quantity
    customField = item.GetCustomField(cf)
    if quantity and customField.Value:
        return quantity * customField.Value


def copyDown(context, cf, prices_dict):
    '''
        Copies % of MSRP from Main Item to it's discountable line items
        param Quote2Context context: context for current quote
        param string cf: needed custom field name as string
		param dict prices_dict: key - Part_number, values - object from sql table row
    '''
    quote_items = context.Quote.GetAllItems()
    main_item = None
    for item in quote_items:
        part_num = item.PartNumber
        if part_num not in prices_dict:
            continue
        if not item.IsLineItem:
            main_item = item
            continue
        if main_item and item.ParentItemId == main_item.Id and prices_dict[part_num].Discountable:
            item[cf] = main_item[cf]


def get_DZ_CUSTOM_PRICE_LIST(context):
    '''
        Gets a list from DZ_CUSTOM_PRICE_LIST custom table, and makes it a dict with Part_number as key, 		 and sql table row as object
        param Quote2Context context: context for current quote
    '''
    quote_items = context.Quote.GetAllItems()
    part_num_list = [item.PartNumber for item in quote_items]
    if not part_num_list:
        return {}
    part_nums_str = "', '".join(part_num_list)
    sql_query = '''SELECT MSRP, DNET, Part_number, Discountable
                   FROM DZ_CUSTOM_PRICE_LIST 
                   WHERE Part_number IN ('{}')'''.format(part_nums_str)
    prices = SqlHelper.GetList(sql_query)
    return {p.Part_number: p for p in prices}
