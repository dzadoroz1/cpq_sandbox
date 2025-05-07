selection = {}
condition_pn = None
av_action = None
delta_pn = None

Trace.Write("wazzup")
Trace.Write(str(dir(context)))

if Session["prev_selection"]:
    selection = Session["prev_selection"]
    condition_pn = Session["condition_pn"]
    av_action = Session["av_action"]

for a in Product.Attributes:
    for av in a.Values:
        if av.IsSelected != selection.get(av.ValueCode,False):
            Trace.Write("delta found {}".format(av.ValueCode))
            delta_pn = av.ValueCode
            Log.Info('see av_action', "true" if av_action else "false")
            if av_action:
                #av.DescriptionFormula = "la la la la"
                av.Display = av.Display + "*" + condition_pn
                #av.TranslatedDisplay += "**"
                #av.UserInput += "++"
                Trace.Write("AUTOSELECT:{}".format(av.ValueCode))
            else:
                av.Display = av.Display.split('*')[0]
        selection[av.ValueCode] = av.IsSelected

if delta_pn:
    Product.Attr("toro_last_selection").HintFormula = delta_pn + "  cond:"+ str(condition_pn) + "  act:"+str(av_action)
    Product.Attr("toro_last_selection").DescriptionFormula  = delta_pn
    
Session["prev_selection"]=selection
#cleanup of condition
Session["condition_pn"]=None
Session["av_action"]=None