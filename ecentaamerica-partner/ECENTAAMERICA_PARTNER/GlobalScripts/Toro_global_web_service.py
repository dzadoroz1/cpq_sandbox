from Toro_link_PB_with_CPL import combineCplAndPrice

partNumber = Param.data["partNumber"]
market = Param.data["market"]
priceBook = Param.data["priceBook"]

CPLPriceList = combineCplAndPrice(partNumber, market, priceBook)

ApiResponse = ApiResponseFactory.JsonResponse(CPLPriceList)
