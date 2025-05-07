#Method to add row in line item container 'Selected Bundle'
#Adds BundleName,NewValue,ProjectedCount
def addNewBundle(LineItems, BundleName, NewValue, ProjectedCount, MaterialCode):
	newItem = LineItems.AddNewRow(str(MaterialCode) + "_cpq", True)
	#Assign attr values
	newItem.Product.Attr("Description").AssignValue(BundleName)
	newItem.Product.Attr("Minimum Commit").AssignValue(str(NewValue))
	newItem.Product.Attr("Projected Count").AssignValue(str(ProjectedCount))	
	newItem.Product.Attr("Material Code").AssignValue(MaterialCode)	
	newItem.Product.ApplyRules()
	newItem.ApplyProductChanges()
	newItem.Calculate()

###########
##Script
###########

def execBundleUpdate(NewValue, LineItems, EventArgs, ChangedRow, BundleName, ProjectedCount, MinimumCount, MaterialCode, Product):

	#Column is minimum commit that was changed and the value is not 0
	#New bundle selected
	#If value is greater
	if MinimumCount > 0 or (EventArgs.ChangedCell.ColumnName == 'Total_Projected' and ProjectedCount> 0 and MinimumCount == 0):
		#Check for promo
		promotions = SqlHelper.GetFirst("SELECT * FROM PROMOTIONS WHERE PROMOTION_TYPE = 'QUANTITY' AND MATERIAL = '{}'".format(MaterialCode))
		if promotions:
			if float(promotions.QUANTITY) <= NewValue:
				Product.Messages.Add("You are qualify for {} promotion at {} minimum commit".format(promotions.PROMO_NAME, promotions.QUANTITY))
			else:
				Product.Messages.Add("You are eligible for {} promotion at {} minimum commit".format(promotions.PROMO_NAME, promotions.QUANTITY))
		
		#Check if item exists in line item
		if LineItems.Rows.Count > 0:
			if LineItems.Rows.GetByColumnName('Material_Code', MaterialCode):
				#Update Line Item
				itemRow = LineItems.Rows.GetByColumnName('Material_Code', MaterialCode)
				itemRow.Product.Attr("Minimum Commit").AssignValue(str(MinimumCount))
				itemRow.Product.Attr("Projected Count").AssignValue(str(ProjectedCount))
				itemRow.Product.Attr("ItemQuantity").AssignValue('')
				itemRow.Product.ApplyRules()
				itemRow.ApplyProductChanges()
				itemRow.Calculate()
			else:
				#Add bundle line item
				addNewBundle(LineItems,BundleName, NewValue, ProjectedCount, MaterialCode)
		else:
			#Add bundle line item
			addNewBundle(LineItems, BundleName, NewValue, ProjectedCount, MaterialCode)

	#Delete line item if minimum commit new value is 0
	if EventArgs.ChangedCell.ColumnName == 'Minimum_Commit' and MinimumCount == 0 :
		#Delete item from Selected Bundles Container
		LineItems.DeleteRow(LineItems.Rows.GetByColumnName('Material_Code', MaterialCode).RowIndex)
		
		#Assign 0 to the projected count in the display bundle container
		ChangedRow.SetColumnValue("Total_Projected","0")
		ChangedRow.Calculate()
	
	#########################################
	##CONSTRUCT FEATURES LIST
	#########################################
	if LineItems.Rows.Count > 0:
		MaterialCode = []
		for row in LineItems.Rows:
			MaterialCode.append(row.GetColumnByName("Material_Code").Value)


		##GET ALL RELEVANT FEATURES
		SQL = "SELECT DISTINCT CAPABILITY FROM PRODUCT_CATALOG_DATA WHERE SHOWINCONFIG ='1' AND MATERIAL_CODE IN {}".format(str(MaterialCode).replace('[','(').replace(']',')'))
		Trace.Write(SQL)
		features = SqlHelper.GetList(SQL)
		##GET FEATURES IN THE LIST
		#LOOP FEATURES

		featureString = '<table style="width:100%"><tr class="table-heading"> <td scope="row" style="width:14%">Minimum Commit </td><td scope="row" style="width:14%">Projected Usage</td><td>Resulting features being ordered</td></tr><tr>'

		endString = '</table>'
		
		for feature in features:
			Projected = 0
			Minimum = 0
			#LOOP SELECTED BUNDLES
			for item in LineItems.Rows:
				if SqlHelper.GetFirst("SELECT SHOWINCONFIG FROM PRODUCT_CATALOG_DATA WHERE SHOWINCONFIG = '1' AND CAPABILITY = '{}' AND MATERIAL_CODE = '{}'".format(feature.CAPABILITY, item.Product.Attr("Material Code").GetValue())):
					Trace.Write(item.GetColumnByName("Minimum_Commit").Value + " CHECK HERE " + item.GetColumnByName("Total_Projected").Value )
					Minimum += int(item.GetColumnByName("Minimum_Commit").Value.replace(',',''))
					Projected += int(float(item.GetColumnByName("Total_Projected").Value))
				
			#Contruct feature line
			featureString +='<td class="responder-line-items">' + str(Minimum) + '</td><td class="responder-line-items">' + str(Projected) + '</td><td class="responder-line-items">' + feature.CAPABILITY + '</td></tr><tr>'
			
		Product.Attr("Features").AssignValue(featureString + endString)
	else:
		Product.Attr("Features").AssignValue('')