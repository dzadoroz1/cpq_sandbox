program = context.Quote.GetCustomField("Pricing_Training_Program_dz")
values_list = SqlHelper.GetFirst("SELECT offMSRP, offDNET, GP, TotalAward FROM DZ_Toro_Pricing WHERE PricingProgram = '{}'".format(program.AttributeValue))

if values_list:
    GP = values_list.GP
    offDNET = values_list.offDNET
    offMSRP = values_list.offMSRP
    TotalAward = values_list.TotalAward

    for item in context.Quote.GetAllItems():
        items_GP = item.GetCustomField("DZ_GP")
        items_offDNET = item.GetCustomField("DZ_DNET")
        items_offMSRP = item.GetCustomField("DZ_MSRP")
        items_TotalAward = item.GetCustomField("DZ_AWARD")

        items_GP.Value = GP
        items_offDNET.Value = offDNET
        items_offMSRP.Value = offMSRP
        items_TotalAward.Value = TotalAward

# set method to none
method = context.Quote.GetCustomField("Program_Training_Method_dz")
method.Value = ""
Trace.Write(method.AttributeValue)