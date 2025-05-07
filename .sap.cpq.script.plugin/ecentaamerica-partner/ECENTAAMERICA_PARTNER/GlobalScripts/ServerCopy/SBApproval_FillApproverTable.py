if context.TabId == 55 :
	Trace.Write("Coontext : " + str(dir(context)))
	currentPtypes = context.Quote.ProductTypes
	SB_approverTable = context.Quote.QuoteTables['Approved_Special_Bid_Discount']

	if SB_approverTable.Rows.Count == 0 : 
		for pType in currentPtypes :
			
			row = SB_approverTable.AddNewRow()
			Trace.Write("MPG : " + pType.ProductTypeName)
			row.SetColumnValue("MPG", pType.ProductTypeName)
			row.SetColumnValue("Description", pType.ProductTypeName )
			Trace.Write("ProductTypeName : " + pType.ProductTypeName)
			type = SqlHelper.GetSingle("SELECT CategoryID, CategoryName from SB_MPGTOCATEGORY WHERE MPG ='" + pType.ProductTypeName + "'")
			Trace.Write("Type : " + type.ToString())
			row.SetColumnValue("Type", type.CategoryName)
	else :

		for pType in currentPtypes : 
			prodTypeFound = False
			for row in SB_approverTable.Rows : 
				mpgID = row.GetColumnValue("MPG") 
				if mpgID == pType.ProductTypeName : 
					row.SetColumnValue("MPG", pType.ProductTypeName)
					row.SetColumnValue("Description", pType.ProductTypeName)
					type = SqlHelper.GetSingle("SELECT CategoryID, CategoryName from SB_MPGTOCATEGORY WHERE MPG ='" + pType.ProductTypeName + "'")
					Trace.Write("Type : " + type.ToString())
					row.SetColumnValue("Type", type.CategoryName)
					prodTypeFound = True
			if prodTypeFound == False : 
				rowNew = SB_approverTable.AddNewRow()
				Trace.Write("MPG : " + pType.ProductTypeName)
				rowNew.SetColumnValue("MPG", pType.ProductTypeName)
				rowNew.SetColumnValue("Description", pType.ProductTypeName )
				Trace.Write("ProductTypeName : " + pType.ProductTypeName)
				type = SqlHelper.GetSingle("SELECT CategoryID, CategoryName from SB_MPGTOCATEGORY WHERE MPG ='" + pType.ProductTypeName + "'")
				Trace.Write("Type : " + type.ToString())
				rowNew.SetColumnValue("Type", type.CategoryName)