context.Quote.GetCustomField('Promotion Approval Required').Value = '0'
sbRequestTable = context.Quote.QuoteTables['Promotions']
for row in sbRequestTable.Rows :
	if row.GetColumnValue("Select") == True:
		if row.GetColumnValue("Approval_Required") == True:
			context.Quote.GetCustomField('Promotion Approval Required').Value = '1'