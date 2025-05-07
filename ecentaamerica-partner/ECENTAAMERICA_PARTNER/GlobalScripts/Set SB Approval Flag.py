context.Quote.GetCustomField('SB Approval Required').Value = '0'
sbRequestTable = context.Quote.QuoteTables['Special_Bid_Request']
for row in sbRequestTable.Rows :
	reqDiscount = row.GetColumnValue("Requested_Discount")
	if reqDiscount > 0:
		context.Quote.GetCustomField('SB Approval Required').Value = '1'
