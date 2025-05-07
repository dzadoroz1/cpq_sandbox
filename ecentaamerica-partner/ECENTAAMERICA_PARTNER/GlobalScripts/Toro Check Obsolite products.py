for a in Product.Attributes:
    if a.SelectedValue:
        if 'obsolete' in a.SelectedValue.Display or 'Obsolete' in a.SelectedValue.Display:
            if a.Name != 'Reelmaster 5010-H drilldown':
                #Trace.Write(a.SelectedValue.Display)
                Product.Messages.Add('Obsolite product selected:'+str(a.SelectedValue.Display))