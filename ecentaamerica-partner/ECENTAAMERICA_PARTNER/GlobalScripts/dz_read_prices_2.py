# After adding products to quote
from dz_module_for_calc import get_DZ_CUSTOM_PRICE_LIST

target_part_num = "LP-B-500GB-24GB-M3-16i"
if User.UserType.Name == "DZ_userType":
    quote_items = context.Quote.GetAllItems()
    main_item = next((item for item in quote_items if item.PartNumber == target_part_num), None)
    if not main_item:
        exit()
    main_item_proc_msrp = main_item["DZ_MSRP"]
    prices_dict = get_DZ_CUSTOM_PRICE_LIST(context)
    for item in quote_items:
        if item.Id != main_item.Id and item.ParentItemId != main_item.Id:
            continue
        part_num = item.PartNumber
        if part_num not in prices_dict:
            continue
        price_data = prices_dict[part_num]
        item["DZ_MSRP_2"] = price_data.MSRP
        item["DZ_DNET_2"] = price_data.DNET
        if not price_data.Discountable:
            item["DZ_MSRP"] = 0
            continue
        item["DZ_MSRP"] = main_item_proc_msrp
