program = context.Quote.GetCustomField("Pricing_Training_Program_dz")
method = context.Quote.GetCustomField("Program_Training_Method_dz")
methods_list = SqlHelper.GetList("SELECT Method FROM DZ_FilterPricingProgram WHERE Program = '{}'".format(program.AttributeValue))