selection = {}
if Session["prev_selection"]:
    selection = Session["prev_selection"]
delta_pn = None
condition_pn = None
av_action = None

for a in Product.Attributes:
    for av in a.Values:
        if av.IsSelected != selection.get(av.ValueCode,False):
            Trace.Write("delta found {}".format(av.ValueCode))
            delta_pn = av.ValueCode
            condition_pn = av.ValueCode
            av_action = av.IsSelected
        selection[av.ValueCode] = av.IsSelected

if delta_pn:
    Product.Attr("toro_last_selection").HintFormula = delta_pn + "  cond:"+ str(condition_pn) + "  act:"+str(av_action)
    Product.Attr("toro_last_selection").DescriptionFormula  = delta_pn
    
    
Session["prev_selection"]=selection
Session["condition_pn"]=condition_pn
Session["av_action"]=av_action