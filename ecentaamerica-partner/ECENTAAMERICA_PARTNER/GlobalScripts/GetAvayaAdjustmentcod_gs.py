for attribute in context.Product.Attributes:
	Trace.Write('*** ATTRIBUTE: '  + attribute.Name + ' ***')
	
if context.Product.Attributes.GetByName('Adjustment Code') is not None:
	adjcode = context.Product.Attributes.GetByName('Adjustment Code').GetValue()
	for item in context.Items:
		x= str(dir(item))
		Trace.Write(x)
		item['AdjustmentCode'] = adjcode


#for item in context.Quote.Items:
#	item['Adjustment Code'] = 'abc'


x= str(dir(context))
Trace.Write(x)


