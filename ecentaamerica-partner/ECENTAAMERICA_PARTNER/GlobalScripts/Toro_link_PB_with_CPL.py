def combineCplAndPrice(partNumber, market, priceBook):
    if partNumber:
        rawResult = SqlHelper.GetList(
            "SELECT CPL.model, CPL.part_number, CPL.attribute, CPL.description, PB.Cost, PB.Price "
            "FROM TORO_CPL_PRICE as CPL "
            "JOIN {0} as PB ON PB.PartNumber = CPL.part_number "
            "WHERE CPL.part_number='{1}'".format(priceBook, partNumber)
        )
        transformed_result = _transformSQLResponse(rawResult)
        return transformed_result

    rawResult = SqlHelper.GetList(
        "SELECT CPL.model, CPL.part_number, CPL.attribute, CPL.description, PB.Cost, PB.Price "
        "FROM TORO_CPL_PRICE as CPL "
        "JOIN {0} as PB ON PB.PartNumber = CPL.part_number".format(priceBook)
    )
    transformed_result = _transformSQLResponse(rawResult)
    return transformed_result

def _transformSQLResponse(raw_data):
    result = []
    for row in raw_data:
        transformed_row = {}
        for item in row:
            transformed_row[item.Key] = item.Value
        result.append(transformed_row)
    return result