from Scripting import SqlDbType

def updateSimpleProductPropertyTable(prod):
    trueBIT = 1
    yesString = "YES"
    falseBIT = 0
    tablerow = dict(
            PartNumber=prod.PartNumber,
            TractionUnit=falseBIT,
            Discountable=falseBIT,
            ExcludeFromRebate=falseBIT,
            ExcludeFromCPL=falseBIT,
            Obsolete=falseBIT,
            NonToroProduct=falseBIT,
            PerformancePart=falseBIT,
            ProductTier="",
            ImageURL="",
            CustomInfoText="",
            ProductType=prod.Type.Name
        )
    sql_query = "SELECT CpqTableEntryId FROM SIMPLEPRODUCTPROPERTIES WHERE PartNumber = @PartNumberProperty"
    tableInfo = SqlHelper.GetTable("SIMPLEPRODUCTPROPERTIES")
    existingProduct = SqlHelper.GetFirst(sql_query, SqlHelper.CreateParameter(prod.PartNumber, "@PartNumberProperty", SqlDbType.NVarChar))

    if existingProduct and existingProduct.CpqTableEntryId:
        tablerow['CpqTableEntryId'] = existingProduct.CpqTableEntryId
    for attr in prod.Attributes:
        attrName = attr.Name.replace(" ", "")
        if attrName in tablerow:
            if not attr.SelectedValue:
                if tablerow[attrName] == "" and attr.Values:
                    for attrValue in attr.Values:
                        if attrValue.IsPreselected:
                            tablerow[attrName] = attrValue.UserInput
                continue
            display = attr.SelectedValue.Display.strip().upper()
            if display == yesString:
                tablerow[attrName] = trueBIT
            elif tablerow[attrName] == falseBIT: # Excludes attribute display values other YES being added in BIT fields. Verifies that the attribute value is free string input
                continue
            else:
                tablerow[attrName] = attr.SelectedValue.UserInput
    tableInfo.AddRow(tablerow)
    SqlHelper.Upsert(tableInfo)