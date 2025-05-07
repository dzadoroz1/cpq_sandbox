list_of_context = dir(context) #receive all method and properties of current context
Log.Info('list of context',str(list_of_context))
list_of_qu = dir(context.Quote) #receive all method and properties of current context
Log.Info('list of quote ',str(list_of_qu))
list_of_quote = dir(context.Quote.GetAllItems) #receive all method and properties of current context
Log.Info('list of quote all items',str(list_of_quote))
for k in context.Quote.GetAllItems():
    Log.Info('quote item', str(dir(k)))
    Log.Info('quote item item', str(dir(k.Item)))
    k.GetCustomField('ToroDiscountable').Value = ''
    Log.Info('quote subitem', str(k.IsSubItem))
    Log.Info('ProductName', k.ProductName)
    if k.IsSubItem:
    	k.GetCustomField('ToroDiscountable').Value = 'True'
    	Log.Info('quote item details', k.GetCustomField('ToroDiscountable').Value)
list_of_Items = dir(context.Items) #receive all method and properties of current context
Log.Info('list of items',str(list_of_Items))
list_of_Product = dir(context.Product) #receive all method and properties of current context
Log.Info('list of Products',str(list_of_Product))