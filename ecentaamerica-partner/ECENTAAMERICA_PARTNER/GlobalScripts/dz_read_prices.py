# After adding products to quote, After updating products in quote
if User.UserType.Name == "DZ_userType":
    part_num_list = [item.PartNumber for item in context.Quote.GetAllItems()]
    part_nums_str = "', '".join(part_num_list)
    sql_query = '''SELECT MSRP, DNET, Part_number 
					FROM DZ_CUSTOM_PRICE_LIST 
					WHERE Part_number IN ('{}')'''.format(part_nums_str)
    prices = SqlHelper.GetList(sql_query)
    prices_dict = {p.Part_number: p for p in prices}
    for item in context.Quote.GetAllItems():
        part_num = item.PartNumber
        if part_num in prices_dict:
            price_data = prices_dict[part_num]
            msrp = item.GetCustomField("DZ_MSRP_2")
            dnet = item.GetCustomField("DZ_DNET_2")
            award = item.GetCustomField("DZ_AWARD_2")
            if msrp and dnet and award:
                msrp.Value = price_data.MSRP
                dnet.Value = price_data.DNET
