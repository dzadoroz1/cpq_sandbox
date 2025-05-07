'''
Trace.Write("EVENT CONTEXT")
Trace.Write(str(dir(context)))
Trace.Write(context.TabId)
'''

promoTable = context.Quote.QuoteTables['Promotions']
nonqualifiedTable = context.Quote.QuoteTables['Non_qualified_promos']

for row in promoTable.Rows:
	if row.GetColumnValue("Promotion_Type") != 'ANY':
		promoTable.DeleteRow(row.Id)
promotions = SqlHelper.GetList("SELECT * FROM PROMOTIONS WHERE PROMOTION_TYPE = 'ANY'")

##These will never change per quote since they're ANY PROMOTION TYPE
##Never remove
if promoTable.Rows.Count == 0:
	for promo in promotions:
		row = promoTable.AddNewRow()
		row.SetColumnValue("Promo_Code", promo.PROMO_CODE)
		row.SetColumnValue("Promo_Name", promo.PROMO_NAME)
		row.SetColumnValue("Promo_Details", promo.PROMO_DETAILS)
		row.SetColumnValue("Total_Discount", float(promo.TOTAL_DISCOUNT))
		row.SetColumnValue("Approval_Required", promo.APPROVAL_REQUIRED == 'Y')
		row.SetColumnValue("Promotion_Type", "ANY")
		
	promoTable.Save()
	
##PROMOTION TYPE : REGION

if context.Quote.BillToCustomer is not None:
	promotions = SqlHelper.GetList("SELECT * FROM PROMOTIONS WHERE PROMOTION_TYPE = 'REGION' and REGION = '{}'".format(context.Quote.BillToCustomer.Country))

	##These will never change per quote since they're ANY PROMOTION TYPE
	##Never remove
	for promo in promotions:
		row = promoTable.AddNewRow()
		row.SetColumnValue("Promo_Code", promo.PROMO_CODE)
		row.SetColumnValue("Promo_Name", promo.PROMO_NAME)
		row.SetColumnValue("Promo_Details", promo.PROMO_DETAILS)
		row.SetColumnValue("Total_Discount", float(promo.TOTAL_DISCOUNT))
		row.SetColumnValue("Approval_Required", promo.APPROVAL_REQUIRED == 'Y')
		row.SetColumnValue("Promotion_Type","REGION")

	promoTable.Save()


##PROMOTION TYPE : MATERIAL AND MATERIAL QUANTITY
for item in context.Items:
	#MATERIAL PROMO
	promotions = SqlHelper.GetList("SELECT * FROM PROMOTIONS WHERE PROMOTION_TYPE = 'Material' AND MATERIAL = '{}'".format(item.PartNumber))

	if promotions.Count != 0:
		for promo in promotions:
			row = promoTable.AddNewRow()
			row.SetColumnValue("Promo_Code", promo.PROMO_CODE)
			row.SetColumnValue("Promo_Name", promo.PROMO_NAME)
			row.SetColumnValue("Promo_Details", promo.PROMO_DETAILS)
			row.SetColumnValue("Total_Discount", float(promo.TOTAL_DISCOUNT))
			row.SetColumnValue("Approval_Required", promo.APPROVAL_REQUIRED == 'Y')
			row.SetColumnValue("Promotion_Type", "MATERIAL")
			row.SetColumnValue("Material", item.PartNumber)
			
		promoTable.Save()
	
	#MATERIAL QUANTITY PROMO
	promotions = SqlHelper.GetList("SELECT * FROM PROMOTIONS WHERE PROMOTION_TYPE = 'QUANTITY' AND MATERIAL = '{}'".format(item.PartNumber))
	
	if promotions.Count != 0:
		for promo in promotions:
			if float(promo.QUANTITY) <= item.Quantity:
				row = promoTable.AddNewRow()
				row.SetColumnValue("Promo_Code", promo.PROMO_CODE)
				row.SetColumnValue("Promo_Name", promo.PROMO_NAME)
				row.SetColumnValue("Promo_Details", promo.PROMO_DETAILS)
				row.SetColumnValue("Total_Discount", float(promo.TOTAL_DISCOUNT))
				row.SetColumnValue("Approval_Required", promo.APPROVAL_REQUIRED == 'Y')
				row.SetColumnValue("Promotion_Type", "QUANTITY")
				row.SetColumnValue("Material", item.PartNumber)
			else:
				row = nonqualifiedTable.AddNewRow()
				row.SetColumnValue("Promo_Code", promo.PROMO_CODE)
				row.SetColumnValue("Promo_Name", promo.PROMO_NAME)
				row.SetColumnValue("Promo_Details", promo.PROMO_DETAILS)
				row.SetColumnValue("Total_Discount", float(promo.TOTAL_DISCOUNT))
				row.SetColumnValue("Reason", "Quantity threshold not met")
				row.SetColumnValue("Material", item.PartNumber)
		promoTable.Save()