from Scripting.Quote import MessageLevel
if User.UserName == "Uldis.Kalviskis@ecenta.com":
    q = context.Quote
    parties = list(q.GetInvolvedParties())
    c = len(parties)

    init_sp = (c == 1 and parties[-1].PartnerFunctionKey == "SP")
    
    if init_sp:
        q.AddInvolvedParty("SH",1)
        q.AddInvolvedParty("BP",1)
        q.AddInvolvedParty("PY",2)
        
    #message level tests
    q.AddMessage("The information",MessageLevel.Info,True)
    q.AddMessage("The warning",MessageLevel.Warning,True)
    q.AddMessage("The error",MessageLevel.Error,True)
    q.AddMessage("The success",MessageLevel.Success,True)