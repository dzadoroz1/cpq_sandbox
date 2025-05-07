##Get product
#for attribute in context.Product.Attributes:
	#Trace.Write('*** ATTRIBUTE: '  + attribute.Name + ' ***')

#Trace.Write(context.Product.Name)
Trace.Write(str(context.Quote))
'''
if context.Product.Attributes.GetByName('Length of Contract') is not None: 
	LengthofContract = context.Product.Attributes.GetByName('Length of Contract').SelectedValue.ValueCode



Trace.Write('LengthofContract' + '   ' + str(LengthofContract))
context.Quote.GetCustomField('Length of Contract').Value = str(LengthofContract)
'''

if context.Product.Name == 'Avaya OneCloud Public CCaaS':
	Trace.Write("Attempting")
	if context.Product.Attributes.GetByName('Length of Contract') is not None:
		#Trace.Write(context.Product.Attributes.GetByName('Length of Contract').GetValue())
		LengthofContract = context.Product.Attributes.GetByName('Length of Contract').SelectedValue.ValueCode
		context.Quote.GetCustomField('Length of Contract').Value = str(LengthofContract)
	if context.Product.Attributes.GetByName('Payment Frequency') is not None:
		PaymentFreq = context.Product.Attributes.GetByName('Payment Frequency').SelectedValue.ValueCode
		context.Quote.GetCustomField('Payment Frequency').Value = str(PaymentFreq)
# transfer also Adjustment Code wo Tier
	if context.Product.Attributes.GetByName('Adjustment Code wo tier') is not None:
		aCode = context.Product.Attributes.GetByName('Adjustment Code wo tier').SelectedValue.Display
		Trace.Write("ACode: " + aCode)
		context.Quote.GetCustomField('ACode').Value = str(aCode)