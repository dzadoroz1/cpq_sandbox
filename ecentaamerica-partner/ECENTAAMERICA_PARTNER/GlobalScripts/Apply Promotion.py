#Trace.Write("APPLYING PROMOTION")
#Trace.Write(str(dir(context)))
#Trace.Write(str(context.TabId))
    
    
#context.Quote.Calculate("Quantity")
##TAB ID 54 is PROMOTIONS TAB
##TAB ID 55 is SPECIAL BIDS
##TAB ID 5 is QUOTATIONS TAB
if context.TabId == 5 and context.Quote.GetCustomField('SB Approval Required').Value == '0':
	Trace.Write("Resetting Discount Amount and Percent")
	for item in context.Quote.GetAllItems():
		item["AVAYAPromotionDiscountAmount"] = 0
		item["AVAYAPromotionDiscountPercent"] = 0
    #Get table
	promoTable = context.Quote.QuoteTables['Promotions']

	
	for row in promoTable.Rows:
		if row.GetColumnValue("Select") == True:
			Trace.Write("Found Selected Row")
			changedRow = row
			#Get the type of promotion
			promoType = changedRow.GetColumnValue("Promotion_Type")
            #ANY #REGION

            #MATERIAL
			if promoType == 'MATERIAL' or promoType == 'QUANTITY':
				material = changedRow.GetColumnValue("MATERIAL")
				Trace.Write("Iterating through items to find material")
				for item in context.Quote.GetAllItems():
					if material == item.PartNumber:
						Trace.Write("Found material and assigning values")
						item["AVAYAPromotionDiscountAmount"] = changedRow.GetColumnValue("Total_Discount")
						item["AVAYAPromotionDiscountPercent"] = (changedRow.GetColumnValue("Total_Discount") / item["TotalContractTermNetPrice"]) * 100

			if promoType == 'ANY' or promoType == 'REGION':
				context.Quote.Totals.Amount = float(context.Quote.Totals.Amount) - changedRow.GetColumnValue("Total_Discount")
			break

context.Quote.Calculate("AVAYAPromotionDiscountAmount")

