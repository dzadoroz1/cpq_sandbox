# contract = context.Quote.GetCustomField('Toro_Contract').Value
# distributor = context.Quote.GetCustomField('Toro_Distributor').Value


# for item in context.Quote.GetAllItems():
#     if not item.IsLineItem :
#         totalMSRP = 0.00
#         totalDNET = 0.00
#         totalAwardPrice = 0.00
#         totalGrossAmount = 0.00
#         totalRebateAmount = 0.00
#         childItems = item.AsMainItem.GetChildItems()
#         for child in childItems:
#             if child.ListPrice > 0 :
#                 child["ToroMSRP"] = child.ListPrice
#                 totalMSRP += child.Quantity * child.ListPrice
#                 child["ToroDNETAmount"] = child.Cost
#                 totalDNET += child.Quantity * child.Cost
#                 Tier = SqlHelper.GetFirst("SELECT Tier FROM Toro_Tiers WHERE SKU = '" + child.PartNumber + "'")
#                 if Tier :
#                     sqlQuery = SqlHelper.GetFirst("SELECT Rebate, Discount FROM Toro_PriceContract WHERE Contract = '" + contract + "' AND Distributor = '" + distributor + "' AND Tier = '" + Tier.Tier + "'")
#                     if sqlQuery:
#                         child['ToroAwardPrice2'] = child.ListPrice * ( 1 - float(sqlQuery.Discount) / 100 )
#                         child.DiscountPercent = ((child.ListPrice - child["ToroAwardPrice2"]) / child.ListPrice) * 100
#                         child['ToroExtendedAwardPrice'] = child['ToroAwardPrice2'] * child.Quantity
#                         totalAwardPrice += child['ToroAwardPrice2'] * child.Quantity
#                         child['ToroRebatePercent'] = float(sqlQuery.Rebate)
#                         child['ToroRebateAmount'] = child['ToroAwardPrice2'] * ( float(sqlQuery.Rebate) / 100 )
#                         totalRebateAmount += child['ToroRebateAmount'] * child.Quantity
#                         if child.Cost > 0 :
#                             child['ToroDNETPercent'] = child['ToroAwardPrice2'] / child.Cost * 100
#                             child['ToroGrossAmount'] = child['ToroAwardPrice2'] - child.Cost + child['ToroRebateAmount']
#                             totalGrossAmount += child['ToroGrossAmount'] * child.Quantity
#                             child['ToroGrossPercent'] = child['ToroGrossAmount'] / child['ToroAwardPrice2'] * 100
#         item["ToroMSRP"] = totalMSRP
#         item["ToroDNETAmount"] = totalDNET
#         item["ToroDNETPercent"] = totalAwardPrice / totalDNET * 100 
#         item['ToroAwardPrice2'] = totalAwardPrice
#         item['ToroExtendedAwardPrice'] = totalAwardPrice * item.Quantity
#         item['ToroGrossAmount'] = totalGrossAmount
#         item['ToroGrossPercent'] = totalGrossAmount / totalAwardPrice * 100
#         item['ToroRebateAmount'] = totalRebateAmount
#         item['ToroRebatePercent'] = totalRebateAmount / totalAwardPrice * 100

quote = context.Quote

#resolve blank selection
if not quote[context.FieldName]:
    quote[context.FieldName] = context.PreviousValue
else:
    items = quote.GetAllItems()
    for item in items:
        #reset award price to triger calculations
        item["ToroAwardPrice2"] = 0.0

    quote.Calculate("ToroAwardPrice2")