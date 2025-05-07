from Scripting import SqlDbType

def _ProcessAndInsertData(product, parentValueCode):
    TPPTrue = 1
    TPPFalse = 0
    tableInfo = SqlHelper.GetTable("CPL")

    for attribute in product.Attributes:
        if attribute.Name == "TPP Term":
            TPPValues = product.Attr("TPP Type").Values
            for attributeValue in attribute.Values:
                for TPPValue in TPPValues:
                    tablerow = {
                        "ProductName": product.Name,
                        "ProductSKU": parentValueCode,
                        "Attribute": "TPP",
                        "SKU": "{}{}-{}".format(TPPValue.ValueCode, attributeValue.ValueCode, parentValueCode),
                        "Description": "TPP {} {}".format(attributeValue.Display, TPPValue.Display),
                        "Type": "TPP {}".format(TPPValue.Display),
                        "TPP": TPPTrue,
                    }

                    tableInfo.AddRow(tablerow)
            continue

        # Avoid making Rows in CPL of Traction Units Product and Traction Units Attribute, TTP (it is handled differently than default), Config Rules, Simple Attribute Question attributes
        if not attribute.IsLineItem or attribute.Name == "TPP_calculated" or attribute.Name == "TPP":
            continue
        
        for attributeValue in attribute.Values:
            # Check if Attribute value (Simple Product) is not excluded from CPL table in SimpleProductProperties Table. Skip for TPP
            sql_query = "SELECT ExcludeFromCPL, ProductType FROM SIMPLEPRODUCTPROPERTIES WHERE PartNumber = @PartNumberProperty" # Update this with ProductType in select statement and add parameter
            simpleProduct = SqlHelper.GetFirst(sql_query, SqlHelper.CreateParameter(attributeValue.ValueCode, "@PartNumberProperty", SqlDbType.NVarChar))
            
            if simpleProduct and simpleProduct.ExcludeFromCPL:
                continue
            
            tablerow = {
                "ProductName": product.Name,
                "ProductSKU": parentValueCode,
                "Attribute": attribute.Name,
                "SKU": attributeValue.ValueCode,
                "Description": attributeValue.Display,
                "Type": simpleProduct.ProductType if simpleProduct and simpleProduct.ProductType else "",
                "TPP": TPPFalse,
            }
            tableInfo.AddRow(tablerow)
    SqlHelper.Upsert(tableInfo)

def updateCPLtable(product):
    queryRowLimit = 1000
    
    # Delete all values associated with the configurable Product to avoid dusplicates, irrelevant attributes and attribute values
    continueDelete = True
    while(continueDelete):
        deleteTableInfo = SqlHelper.GetTable("CPL")
        sql_query = "SELECT CpqTableEntryId FROM CPL WHERE ProductName = @ProductName"
        deleteList = SqlHelper.GetList(sql_query, SqlHelper.CreateParameter(product.Name, "@ProductName", SqlDbType.NVarChar))

        if deleteList:
            for row in deleteList:
                deleteTableInfo.AddRow(row)
            SqlHelper.Delete(deleteTableInfo)

            if len(deleteList) != queryRowLimit:
                continueDelete = False
        else: # edgecase where last 1000 rows were deleted 
            continueDelete = False

    # Supports Model based approach. Used to catch Config Products with no Traction Units     
    tractionUnitExists = False
    for TractionUnitAttr in product.Attributes:
        # Skip non-Traction Unit Attributes
        if not "TRACTION UNIT" in TractionUnitAttr.Name.upper():
            continue
        tractionUnitExists = True
        
        # Loop over all Traction Units
        for TractionUnitAttrValue in TractionUnitAttr.Values:
            _ProcessAndInsertData(product, TractionUnitAttrValue.ValueCode)        
    if not tractionUnitExists:
        _ProcessAndInsertData(product, product.PartNumber)