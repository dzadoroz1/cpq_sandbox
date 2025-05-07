#not used. Default quantities defined on product attribute level (values tab)
for a in Product.Attributes:
    #Trace.Write(a.Name)
    if a.SelectedValue:
        #Trace.Write(a.SelectedValue.PartNumber)
        sqlString = "SELECT TOP 1 Qty FROM TORO_DEFAULT_QTY where PartNbr = '{0}'".format(a.SelectedValue.PartNumber)
        qty = SqlHelper.GetFirst(sqlString)
        if qty:
            if qty.Qty > 1:
                #Trace.Write(qty.Qty)
                a.Quantity = qty.Qty