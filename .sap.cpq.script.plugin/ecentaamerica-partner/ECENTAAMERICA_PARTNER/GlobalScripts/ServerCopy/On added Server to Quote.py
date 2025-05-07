company_name = User.Company.Name
# Log.Info(company_name)
user_type_name = User.UserType.Name
Log.Info("User Type: " + str(user_type_name))
if user_type_name == 'Salesforce Developer':
    all_items = context.Quote.GetAllItems()
    item_count = len(all_items)
    # Log.Info(str(item_count))
    for item in all_items:
        item_quantity = item.Quantity
        # Log.Info(str(item_quantity))
        if item_count == 2:
            item.DiscountPercent = 10.0
        elif item_count > 2:
            item.DiscountPercent = 15.0
        else:
            item.DiscountPercent = 0.0
        applied_discount = item.DiscountPercent
        # Log.Info("Applied " + str(applied_discount) + "% discount to product: " + str(item.PartNumber))
        list_price = item.ListPrice
        discount_amount = list_price * (applied_discount / 100)
        item.NetPrice = list_price - discount_amount
        item.DiscountAmount = discount_amount

else:
    Log.Info("User's type is not eligible for discounts.")
