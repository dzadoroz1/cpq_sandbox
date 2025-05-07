def count_ext(item, cf):
    quantity = item.Quantity
    customField = item.GetCustomField(cf)
    if quantity and customField.Value:
        return quantity * customField.Value
