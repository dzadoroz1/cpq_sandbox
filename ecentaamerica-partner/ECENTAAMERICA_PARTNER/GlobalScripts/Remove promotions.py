'''
Trace.Write("EVENT CONTEXT")
Trace.Write(str(dir(context)))
Trace.Write(context.TabId)
'''

promoTable = context.Quote.QuoteTables['Promotions']

for item in context.DeletedItems:
    for row in promoTable.Rows:
        if row.GetColumnValue("Material") == item.PartNumber:
            promoTable.DeleteRow(row.Id)