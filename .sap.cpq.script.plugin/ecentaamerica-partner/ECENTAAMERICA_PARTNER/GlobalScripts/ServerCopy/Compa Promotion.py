import Scripting.Quote.MessageLevel
if User.Company.Name == 'Compa Corp':

    quoteItems = context.Quote.GetAllItems()
    quoteItemOverallQuantity = 0
    discountAmount = 0
    MessageLevel = Scripting.Quote.MessageLevel

    for item in quoteItems:
        quoteItemOverallQuantity += item.Quantity
    if quoteItemOverallQuantity == 2:
        discountAmount = 15
    elif quoteItemOverallQuantity >= 3:
        discountAmount = 20
    elif quoteItemOverallQuantity >= 4:
        discountAmount = 20

    for item in quoteItems:
        item.DiscountPercent = discountAmount

    context.Quote.Calculate('Full')