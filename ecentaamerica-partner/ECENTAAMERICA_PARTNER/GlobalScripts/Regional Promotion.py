##PROMOTION TYPE : REGION
promoTable = context.Quote.QuoteTables['Promotions']
for row in promoTable.Rows:
	if row.GetColumnValue("Promotion_Type") == 'REGION':
		promoTable.DeleteRow(row.Id)


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