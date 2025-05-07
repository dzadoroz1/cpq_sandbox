if context.Product.Attributes.GetByName('Adjustment Code') is not None:
	adjcode = context.Product.Attributes.GetByName('Adjustment Code').GetValue()
	for item in context.Items:
		item['AdjustmentCode'] = adjcode

