from Scripting import SqlDbType

for attr in Product.Attributes:
    for b in attr.SelectedValues:
        params =[SqlHelper.CreateParameter(b.PartNumber, "@part_numb", SqlDbType.NVarChar),SqlHelper.CreateParameter("Obsolite", "@attr_name", SqlDbType.NVarChar),]

        obsolite = SqlHelper.GetFirst("SELECT p.* FROM (PRODUCT_ATTRIBUTES pa INNER JOIN ATTRIBUTE_DEFN a ON pa.STANDARD_ATTRIBUTE_CODE  = a.STANDARD_ATTRIBUTE_CODE ) INNER JOIN products p ON pa.PRODUCT_ID  = p.product_id WHERE p.PRODUCT_CATALOG_CODE = @part_numb AND STANDARD_ATTRIBUTE_NAME = @attr_name", *params)
        if (obsolite):
            Product.Messages.Add('Obsolite product selected:'+str(b.Display))