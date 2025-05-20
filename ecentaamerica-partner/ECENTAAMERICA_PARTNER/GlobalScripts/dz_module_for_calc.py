from Scripting.Quote import MessageLevel

def count_ext(item, cf):
    '''
        Calculates extended price by multiplying price with quantity
        Formula: quantity * methodPrice
        param Quote2Item item: item from quote Items collection
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
        param List[IQuoteItem] quote_items: quote items collection
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
        param List[IQuoteItem] quote_items: quote items collection
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


def exceed_100(item, cf, quote):
    '''
    	Validates that % of DNET doesn't exceed 100, if it does the function gives warning and overwrites 		  it with previous value
        param Quote2Item item: item from quote items collection
        param string cf: needed custom field name as string
        param Quote2 quote: quote for the message warning
        return: void
    '''
    if item[cf] <= 100:
        exit()
    quote.AddMessage("100% is a maximum", MessageLevel.Warning, True)
    item[cf] = (item[cf] - item.GetDelta(cf))


def check_non_negative(item, cf, quote):
    '''
    	Validates that % of DNET is non negative, if it does the function gives warning and overwrites 		    it with previous value
        param Quote2Item item: item from quote items collection
        param string cf: needed custom field name as string
        param Quote2 quote: quote for the message warning
        return: void
    '''
    if item[cf] >= 0:
        exit()
    quote.AddMessage("Precent can't be negative", MessageLevel.Warning, True)
    item[cf] = (item[cf] - item.GetDelta(cf))