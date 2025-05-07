list = []
atrributes = Product.Attributes
for attr in atrributes:
    for value in attr.Values:
        list.append(value.Display)

ApiResponse = ApiResponseFactory.JsonResponse(list);