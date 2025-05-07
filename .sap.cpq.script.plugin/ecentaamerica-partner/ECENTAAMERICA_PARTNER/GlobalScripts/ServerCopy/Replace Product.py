if context.Quote:
	#Check if quote has the replacementrequired field set
	if context.Quote.GetCustomField("itemReplacementRequired").Value == '1':
		
		
		#Go through attributes to see if items are selected
		Devices = Product.Attr('One-Time-Purchase AVAYA Devices (Phones)')

		#test = Devices.SelectedValues
		#for value in Devices.SelectedValues:
		#	SelectedDevices.insert(str(value.ValueCode))
		#SelectedDevices = '700513569','700713917'
        
		#Check replace Product
		replacedProducts = SqlHelper.GetList('SELECT * FROM REPLACED_PRODUCTS')
		#test2 = SqlHelper.GetList("SELECT * FROM STANDARD_ATTRIBUTE_VALUES WHERE SYSTEM_ID = '700513569_AVAYA_Devices_1_cpq'")
		
		itemReplacementMessage = ''
		#For item selected
		for item in context.Quote.GetAllItems():
			
			Trace.Write(item.ProductName)
			if item['ItemOrderStatus'] == 'Discontinued':
				itemReplacementMessage += "Item " + item.ProductName + " has been discontinued. Please remove item from the quote. <br>"
				#Product.Messages.Add("Item " + item.ProductName + " has been discontinued. Please remove item from the quote.")
				continue
			if item['ItemOrderStatus'] == 'Replace':
				Trace.Write(item.ProductId)
				#get the replacement system id
				replacedProduct = SqlHelper.GetFirst("SELECT ReplacementSystemId FROM REPLACED_PRODUCTS WHERE OriginalProductId = '{}'".format(item.ProductId))
				
                
				#go through attribute values to see if we can select new replacement item automatically
				for device in Devices.Values:
					Trace.Write(replacedProduct.ReplacementSystemId + ' ' + device.SystemId)
					#get the reference product of attribute line item
					attributeValue = SqlHelper.GetFirst("SELECT ref_product_id FROM STANDARD_ATTRIBUTE_VALUES WHERE SYSTEM_ID = '{}'".format(device.SystemId) )
					
					if attributeValue:
						Trace.Write("TEST: " + str(attributeValue.ref_product_id))
						#if the reference product matches the item that needs to be replace, select and display message to user
						ProductId = ProductHelper.CreateProduct(replacedProduct.ReplacementSystemId).Id
						Trace.Write("TEST PRODUCT ID: " + str(ProductId))
						if attributeValue.ref_product_id == ProductHelper.CreateProduct(replacedProduct.ReplacementSystemId).Id:
							#Trace.Write("SELECT VALUE")
							#SelectedDevices.append(device.ValueCode)
							#String = "'" + "', '".join([str(x) for x in SelectedDevices]) + "'"
							#Devices.SelectValues(True,SelectedDevices)
							itemReplacementMessage += "Item " + item.ProductName + " in your quote has been replaced by " + str(ProductHelper.CreateProduct(replacedProduct.ReplacementSystemId).Name) + "<br>"
							#Product.Attr('ItemReplacementMessage').AssignValue("Item " + item.ProductName + " in your quote has been replaced by " + str(ProductHelper.CreateProduct(replacedProduct.ReplacementSystemId).Name))
		Product.Attr('ItemReplacementMessage').AssignValue(itemReplacementMessage)
	else:
		Product.Attr('ItemReplacementMessage').AssignValue('')