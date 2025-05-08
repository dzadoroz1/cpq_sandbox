def count_ext(item, cf):
    '''
    	Calculates extended price by multipling price with quantity
        Formula: quantity * methodPrice
        param IQuoteItem item: item from quote Items collection
        param string cf: needed custom field name as string
    '''
    quantity = item.Quantity
    customField = item.GetCustomField(cf)
    if quantity and customField.Value:
        return quantity * customField.Value
