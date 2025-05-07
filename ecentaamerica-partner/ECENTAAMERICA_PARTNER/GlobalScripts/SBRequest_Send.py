Trace.Write("writeback context :" + str(dir(context)))
Trace.Write("writeback Quote :" + str(dir(context.Quote)))
Trace.Write("writeback all :" + str(dir()))
#Trace.Write("writeback all :" + str(dir(EventArgs)))

# Check for Mandatory fields 

SBRequestTable = context.Quote.QuoteTables['Special_Bid_Request']
SBQuote = context.Quote

businessJustification = context.Quote.GetCustomField("Business Justification")
requestorsComment = context.Quote.GetCustomField("Requestor Comments") 
typeOfOpportunity = context.Quote.GetCustomField("Type of Opportunity").Value

requestComplete = True

Trace.Write("businessJustification :" + str(dir(businessJustification)))
Trace.Write("businessJustification :" + businessJustification.Value)
if businessJustification.Value == "" :
	Log.Error("Please enter a <b>Business Justification</b> for this Special Bid Request")
	requestComplete = False

if requestorsComment.Value == "" : 
	Log.Error("Please enter a <b>Requestor Comment</b> for this Special Bid Request")
	requestComplete = False

if typeOfOpportunity == "":
	Log.Error("Please select a value in field <b>Type of Opportunity</b> for this Special Bid Request")
	requestComplete = False

#SBRequestTable.ExecuteValidations()

if SBRequestTable.HasValidationsFailed : 
	Log.Error("Please fill all required fields in the <b>Special Bid Request table!</b>")
	requestComplete = False




Trace.Write("Mandatory fields: " + str(requestComplete))
# Determine Approver 

if requestComplete : 

#find Approver
	contractLength = context.Quote.GetCustomField("Length of Contract").AttributeValueCode
	quoteTotalNet = (context.Quote.Totals.MrcNetPrice * float(contractLength)) + context.Quote.Totals.NetPrice
	sqlString = "SELECT Approver from SB_APPROVERDETERMINATION WHERE Theatre ='EU' AND CategoryTotalAPLMin < '" + str(quoteTotalNet) + "' AND CategoryTotalAPLMax >= '" + str(quoteTotalNet) + "' AND CategoryID = 'PROD'" 
	Trace.Write("data for SQL: " + str(dir(quoteTotalNet)) + " : " + str(contractLength) + " : " + sqlString)
	
	approver = SqlHelper.GetFirst(sqlString)
	
	
	if approver : 
		Trace.Write("Approver :" + approver.Approver)
#		sBQuoteCustomFields = SBQuote.CustomFields
		Trace.Write("ApproverID :" + str(dir(context.Quote.GetCustomField("SBApproverID"))))
		approv = context.Quote.GetCustomField("SBApproverID")
        approv.Value = str(approver.Approver)
        

        
# Generate SB Number 
	Trace.Write("Special Bid Number :" + str(dir(SBQuote.GetCustomField("Special Bid Number"))))
	sbID = context.Quote.GetCustomField("Special Bid Number")
	sbID.Value  = str ("SB-" + str(context.Quote.QuoteNumber) + "V1")







