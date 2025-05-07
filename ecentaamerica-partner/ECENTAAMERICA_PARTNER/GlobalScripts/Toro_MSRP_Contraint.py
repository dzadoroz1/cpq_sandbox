from Scripting.Quote import MessageLevel
user_type_name = User.UserName
if user_type_name == "mamedvediev": 
    all_items = context.Quote.GetAllItems() # receive all quote items
    added_items = context.Items
    item_count = len(all_items)
    for item in all_items:
        item_Quantity = item.Quantity
        MAX_QUANTITY = item.Toro_Pricing_Program_Percentage_of_MSRP
        if item_Quantity >= MAX_QUANTITY:
            Log.Info("Quantity exceeds the maximum")
            warning_message = "The maximum allowed quantity is 99. The quantity has been reverted."
            context.Quote.AddMessage(warning_message, MessageLevel.Warning, False)
