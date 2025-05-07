from Scripting import SqlDbType

def _transformSQLResponse(raw_data):
    result = {}
    for row in raw_data:
        transformed_row = {}
        partNumber = ""
        for item in row:
            if item.Key == "PartNumber":
                partNumber = str(item.Value)
                continue
            transformed_row[item.Key] = item.Value
        result[partNumber] = transformed_row
    return result

base_sql_query = """
    SELECT PartNumber, CustomInfoText, Obsolete, ImageURL
    FROM SIMPLEPRODUCTPROPERTIES
    WHERE
"""
sql_res = []
is_conditions = []
parameters = []
sql_query = base_sql_query

i = 0
for attribute in Product.Attributes:
    for value in attribute.Values:
        param_name = "@PartNumber{}".format(i)
        is_conditions.append("PartNumber = {}".format(param_name))
        parameters.append(SqlHelper.CreateParameter(value.ValueCode, param_name, SqlDbType.NVarChar))
    i += 1
# Add the dynamic LIKE conditions to the SQL query
if is_conditions:
    sql_query += " OR ".join(is_conditions)

# Execute the query with all parameters
sql_res = _transformSQLResponse(SqlHelper.GetList(sql_query, *parameters))
ApiResponse = ApiResponseFactory.JsonResponse(sql_res)