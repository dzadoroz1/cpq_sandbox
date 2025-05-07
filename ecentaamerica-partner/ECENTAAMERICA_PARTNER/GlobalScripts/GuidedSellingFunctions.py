def parseAnswer(Product, Attribute, ProductName):
    
	#Container should be cleared before being called here
	GuidedBundles = Product.GetContainerByName("Capabilities")
        
	#Parse the value code of selected questions
    #The value code will store the material code
	#Trace.Write("Checking ATTRIBUTE:" + Attribute)
	if Product.Attr(Attribute).SelectedValue:
		#Trace.Write("ATTRIBUTE FOUND:" + Attribute)
		Ans = Product.Attr(Attribute).SelectedValue.ValueCode.split(' ')

		#Iterate through material code
		#Potential of 1 - 2 material codes
		for item in Ans:
			#Trace.Write(item)
			
			#Query to get the bundle name
			query = "SELECT BUNDLE FROM PRODUCT_CATALOG_DATA WHERE MATERIAL_CODE = '" + item + "' AND OFFER = '" + ProductName + "'"
			itemInfo = SqlHelper.GetFirst(query)
			
			##If there is a matching material code in the product catalog
			if itemInfo:
				#Add Row
				row = GuidedBundles.AddNewRow()
				
				#Add information to row
				row.SetColumnValue("CAPABILITY", itemInfo.BUNDLE)
				row.SetColumnValue("Associated_Bundle", itemInfo.BUNDLE)
				row.SetColumnValue("Associated_MaterialCode", item)
		
#Method for when configuration is loaded		
def parseGuidedSelling(Product, ProductName, AttributeList):
	for attr in AttributeList:
		#Trace.Write(attr)
		parseAnswer(Product, attr, ProductName)