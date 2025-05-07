from update_SimpleProductProperty_table import updateSimpleProductPropertyTable
from update_CPL_table import updateCPLtable

deserialized = JsonHelper.Deserialize(RequestContext.Body)

# Extract the system ID and create a product instance
model = deserialized["SystemId"]
prod = ProductHelper.CreateProduct(model)

parentProduct = SqlHelper.GetFirst(
    "SELECT SYSTEM_ID FROM PRODUCTS WHERE PRODUCT_ID = '{0}'".format(prod.Id)
).SYSTEM_ID
contextProduct = prod.SystemId
isAlias = False
if parentProduct != contextProduct:
    Log.Info(prod.SystemId + ' = Alias of ' + parentProduct)
    isAlias = True

if not isAlias:
    if prod.IsSimple:
        Log.Info("update Simple Product Property Table")
        updateSimpleProductPropertyTable(prod)
    else:
        updateCPLtable(prod)
