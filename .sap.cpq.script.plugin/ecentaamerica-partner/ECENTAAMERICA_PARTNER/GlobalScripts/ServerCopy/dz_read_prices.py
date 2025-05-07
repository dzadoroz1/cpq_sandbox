for item in context.Quote.GetAllItems():
    part_num = item.PartNumber
    prices = SqlHelper.GetFirst("SELECT MSRP, DNET FROM DZ_CUSTOM_PRICE_LIST WHERE Part_number = '{}'".format(part_num))
    if prices:
        msrp = item.GetCustomField("DZ_MSRP_2")
        dnet = item.GetCustomField("DZ_DNET_2")
        award = item.GetCustomField("DZ_AWARD_2")
        if msrp and dnet and award:
            msrp_precent = item.GetCustomField("DZ_MSRP")
            msrp.Value = prices.MSRP
            dnet.Value = prices.DNET
            if msrp_precent.Value: 
                award.Value = msrp_precent.Value * msrp.Value