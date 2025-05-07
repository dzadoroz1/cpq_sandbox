replacedProducts = SqlHelper.GetList('SELECT * FROM REPLACED_PRODUCTS')

ReplacementRequired = 0
for item in context.Quote.GetAllItems():
	item["ItemOrderStatus"] = 'In Stock'
	Discontinued = SqlHelper.GetFirst("SELECT * FROM PRODUCTS WHERE SYSTEM_ID = '{}' AND ENDSTATUS = 1".format(item.ProductSystemId))
    
	if Discontinued:
		item['ItemOrderStatus'] = 'Discontinued'
		ReplacementRequired = 1
		continue

	for replacement in replacedProducts:
		if replacement.OriginalProductId == item.ProductId:
			item["ItemOrderStatus"] = 'Replace'
			ReplacementRequired = 1
			break

context.Quote.GetCustomField('itemReplacementRequired').Value = ReplacementRequired