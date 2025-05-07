
Trace.Write("Context :" + str(dir(context)))
Trace.Write("Quote :" + str(dir(context.Quote)))
sbQuote = context.Quote



if sbQuote.StatusName == "Appoved": 

	sbRequestTable = context.Quote.QuoteTables['Special_Bid_Request']	
	sbApprovalTable = context.Quote.QuoteTables['Approved_Special_Bid_Discount']
	sbQuoteItems = sbQuote.GetAllItems()
	pTypes = context.Quote.ProductTypes
	
	for row in sbApprovalTable.Rows :
		mpg = row.GetColumnValue("MPG")
		approvedDiscount = row.GetColumnValue("Approved_Discount")
		for item in sbQuoteItems :
			if item.ProductTypeName == mpg :
				item["AVAYAPromotionDiscountPercent"] = approvedDiscount
				
	sbQuote.Calculate("AVAYAPromotionDiscountAmount")
	#sbQuote.Calculate("AVAYAPromotionDiscountPercent")
		