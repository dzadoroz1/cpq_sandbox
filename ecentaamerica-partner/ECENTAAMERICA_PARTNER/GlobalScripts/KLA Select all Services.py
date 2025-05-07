ContainerName = "KLA_RENEWAL_SERVICES"
ContainerNameSelected = "KLA_RENEWAL_SERVICES_SELECTED"
ServiceProductsContainer = Product.GetContainerByName(ContainerName)
ServiceProductsContainerSelected = Product.GetContainerByName(ContainerNameSelected)
if ServiceProductsContainer is not None:
	for row in ServiceProductsContainer.Rows:
		new_row = ServiceProductsContainerSelected.AddNewRow(True)
		new_row["Service_Product"] = row["Service_Product"]
		new_row.Product.Attributes.GetByName("KLA Service Product").AssignValue(row["Service_Product"])
		new_row.Product.Attributes.GetByName("KLA Service Program").SelectValue(row["Service_Program"])
		new_row.Product.Attributes.GetByName("KLA Service Program As-Is").SelectValue(row["Service_Program"])
		new_row.Product.Attributes.GetByName("KLA Contract Item Start Date").AssignValue(row["Contract_Item_Start_Date"])
		new_row.Product.Attributes.GetByName("KLA Contract Item End Date").AssignValue(row["Contract_Item_End_Date"])
		new_row.Product.Attributes.GetByName("KLA Total Price").AssignValue(row["Total"])
		new_row.Product.Attributes.GetByName("KLA Contract Type").AssignValue(row["Contract_Type"])
		new_row.Product.Attributes.GetByName("KLA Tool Life Stage").AssignValue(row["Tool_Life_Stage"])
		new_row.Product.Attributes.GetByName("KLA Warranty End Date").AssignValue(row["Warranty_End_Date"])
		new_row.Product.Attributes.GetByName("KLA UTID").AssignValue(row["UTID"])
		new_row.Product.Attributes.GetByName("KLA Product Model").AssignValue(row["Product_Model"])
		new_row.Product.Attributes.GetByName("KLA Product Line").AssignValue(row["Product_Line"])
		new_row.Product.Attributes.GetByName("KLA Product Family").AssignValue(row["Product_Family"])
		new_row.Product.Attributes.GetByName("KLA Contract Number").AssignValue(row["Contract_Number____Padded_"])

		new_row.Product.ApplyRules()
		new_row.ApplyProductChanges()
ServiceProductsContainer.CalculateTotals()
Product.Attributes.GetByName("ItemQuantity").AssignValue(1)
Product.ApplyRules()