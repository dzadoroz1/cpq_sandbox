#Trace.Write(str(dir(context)))
DiscountPercent = SqlHelper.GetFirst("SELECT DISCOUNT_PERCENT FROM CONTRACTUAL_DISCOUNTS WHERE CUSTOMER_CODE = '{}'".format(context.Quote.BillToCustomer.CustomerCode))
if DiscountPercent:
    for item in context.Quote.GetAllItems():
        item.DiscountPercent = float(DiscountPercent.DISCOUNT_PERCENT)
        item.MrcDiscountPercent = float(DiscountPercent.DISCOUNT_PERCENT)
context.Quote.Calculate('DiscountPercent')
context.Quote.Calculate('MrcDiscountPercent')
context.Quote.Calculate('DiscountAmount')
context.Quote.Calculate('MrcDiscountAmount')