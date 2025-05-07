from Scripting import SqlDbType

def deleteTableRows(tableName, column, parameter):
    queryRowLimit = 1000
    
    # Delete all values associated with the configurable Product to avoid dusplicates, irrelevant attributes and attribute values
    continueDelete = True
    while(continueDelete):
        deleteTableInfo = SqlHelper.GetTable("tableName")
        sql_query = "SELECT CpqTableEntryId FROM {} WHERE {} = @parameter".format(tableName, column)
        deleteList = SqlHelper.GetList(sql_query, SqlHelper.CreateParameter(parameter, "@parameter", SqlDbType.NVarChar))

        if deleteList:
            for row in deleteList:
                deleteTableInfo.AddRow(row)
            SqlHelper.Delete(deleteTableInfo)

            if len(deleteList) != queryRowLimit:
                continueDelete = False
        else: # edgecase where last 1000 rows were deleted 
            continueDelete = False