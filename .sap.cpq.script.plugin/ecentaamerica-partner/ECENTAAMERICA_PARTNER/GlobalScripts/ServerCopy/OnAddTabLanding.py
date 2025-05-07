from Scripting.Quote import AccessLevel

if User.UserName == "Uldis.Kalviskis@ecenta.com" and context.TabId == 8:
    q = context.Quote
    acode = q.GetCustomField("ACode")
    acode.AccessLevel = AccessLevel.ReadOnly