#Trace.Write("Context :" + str(dir(context)))
#Trace.Write("Quote :" + str(dir(context.Quote)))
if context.TabId == 55 :
	sbTable = context.Quote.QuoteTables['Special_Bid_Request']	
	currentItems = context.Quote.GetAllItems()
	pTypes = context.Quote.ProductTypes
	dictForAPLValue = {}
	dictForNetValue = {}
	dictForCategory = {}
	contractLength = context.Quote.GetCustomField("Length of Contract").AttributeValueCode
	SBReqRows = sbTable.Rows
	SBQuote = context.Quote
	#Trace.Write("Starting") 

	#Delete table rows

	dictForDiscount = {}


	for row in sbTable.Rows : 
		category = row.GetColumnValue("Special_Bid") 
		discount = row.GetColumnValue("Requested_Discount")
		dictForDiscount[category] = discount
		sbTable.DeleteRow(row.Id)

	#Trace.Write("entering pType")

	for pType in pTypes :
		if pType.MrcListPrice > 0 or pType.ListPrice > 0 :
			pTypeCategory = SqlHelper.GetList("SELECT CategoryID, CategoryName from SB_MPGTOCATEGORY WHERE BACKENDDISC IS NULL AND MPG = '" + pType.ProductTypeName + "'")
			#Trace.Write("MPG" + pType.ProductTypeName)
			if pTypeCategory.Count > 0:
				#Trace.Write("SQLResult : " + str(pTypeCategory.Count) + "CategoryID: " + pTypeCategory[0].CategoryID)
				if pTypeCategory[0].CategoryID in dictForAPLValue: 
				#KEY EXISTS
					dictForAPLValue[pTypeCategory[0].CategoryID] += (pType.ListPrice + (pType.MrcListPrice * float(contractLength)))
					dictForNetValue[pTypeCategory[0].CategoryID] += (pType.NetPrice + (pType.MrcNetPrice * float(contractLength)))
					
				else : 
				#NEW KEY 
					#Trace.Write("NEW KEY" + pTypeCategory[0].CategoryID)
					dictForAPLValue[pTypeCategory[0].CategoryID] = (pType.ListPrice + (pType.MrcListPrice * float(contractLength)))
					dictForNetValue[pTypeCategory[0].CategoryID] = (pType.NetPrice + (pType.MrcNetPrice * float(contractLength)))
					dictForCategory[pTypeCategory[0].CategoryID] = pTypeCategory[0].CategoryName
					

	#Populate table 




	for cat, name in dictForCategory.items() :
	#	Trace.Write("KEY : " + cat + " Name : " + name )
	#	Trace.Write("dictForAPLValue : " + str(dictForAPLValue.get(cat)) + " NetValue: " + str(dictForNetValue.get(cat)))
	#	Trace.Write("Dict :" + str(dir(dictForCategory)))
		newRow = sbTable.AddNewRow()
		newRow.SetColumnValue("Special_Bid", name)
		lv_APL = float(dictForAPLValue.get(cat))
		newRow.SetColumnValue("Category_Total_APL" , lv_APL)
		lv_net = float(dictForNetValue.get(cat))
		newRow.SetColumnValue("Category_Quoted_Net_Amount", lv_net)
		if name in dictForDiscount:
			Trace.Write("found " + name)
			newRow.SetColumnValue("Requested_Discount", dictForDiscount.get(name))
			discamount = dictForDiscount.get(name) / 100 * lv_APL
			newRow.SetColumnValue("Discount_Amount", discamount)
		newRow.SetColumnValue("Discount_Type3","INDINCR")
		newRow.SetColumnValue("Currency", "USD")
		
			
	#	Trace.Write("Creating Row" + cat)

	sbID = context.Quote.GetCustomField("Special Bid Number")

	if sbID.Value == "" :
		sbID.Value  = str ("SB-" + str(context.Quote.QuoteNumber) + "V1")
		
	oppType = context.Quote.GetCustomField("Type of Opportunity")
	if oppType.Value == "" :
		oppType.Value = "PROD"
		
	
	if SBQuote.StatusId >= 11 :
		Trace.Write("Status > 11")
#		rows = sbTable.Rows
#		sbTable.AccessLevel = sbTable.AccessLevel.ReadOnly
		disccolumn = sbTable.GetColumnByName("Discount_Type3")
		disccolumn.AccessLevel = disccolumn.AccessLevel.ReadOnly
		
		discamount = sbTable.GetColumnByName("Discount_Amount")
		discamount.AccessLevel = discamount.AccessLevel.ReadOnly
		
		discperc = sbTable.GetColumnByName("Requested_Discount")
		discperc.AccessLevel = discperc.AccessLevel.ReadOnly
		
		
#		for row in rows :
#			cells = row.Cells
#			for cell in cells :
#				cell.AccessLevel = cell.AccessLevel.ReadOnly
			
			
	
	
	
	sbTable.Save()
	
	
	
	
	