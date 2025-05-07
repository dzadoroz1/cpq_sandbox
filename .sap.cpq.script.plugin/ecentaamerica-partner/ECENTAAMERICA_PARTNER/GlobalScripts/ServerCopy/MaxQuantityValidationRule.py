from Scripting.Quote import MessageLevel
list_of_props = dir(context) #receive all method and properties of current context
Log.Info(str(list_of_props))
MAX_QUANTITY = 99
user_type_name = User.UserName
user_dictionary = User.SelectedDictionary
Log.Info(user_dictionary.Name)
if user_type_name == "mamedvediev":
    Log.Info("Validation Quantity MAX restriction works")
    all_items = context.Quote.GetAllItems() # receive all quote items
    added_items = context.Items # receive only added items
    item_count = len(all_items)
    # Log.Info(str(item_count))
    for item in all_items:
        item_Quantity = item.Quantity
        if item_Quantity >= MAX_QUANTITY:
            Log.Info("Quantity exceeds the maximum")
            #warning_message_key = 'QuantityExceedsMax'
        	#warning_message = context.Quote.UserDictionary.Translate(warning_message_key)
            #if not warning_message:
            warning_message = "The maximum allowed quantity is 99. The quantity has been reverted."
            translated_message = Translation.Get(user_dictionary.Name)
            #translated_message = Translation.Get("Deutsch / German")

            Log.Info(translated_message)
            #context.Quote.AddMessage("message text", MessageLevel.Error, True)
            context.Quote.AddMessage(translated_message, MessageLevel.Warning, False)
            #context.Quote.AddMessage(translated_message, MessageLevel.Warning, False)