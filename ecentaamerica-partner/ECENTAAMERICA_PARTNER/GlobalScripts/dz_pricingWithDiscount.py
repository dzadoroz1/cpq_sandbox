for item in context.Quote.GetAllItems():
    udf = item.GetCustomField("PriceWithDiscount")
    discount = item.DiscountAmount
    udf.Value = item.ExtendedListPrice - discount

# PLUGIN TEST
