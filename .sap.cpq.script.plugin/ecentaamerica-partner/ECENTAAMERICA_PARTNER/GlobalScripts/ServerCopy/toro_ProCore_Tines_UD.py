allowSleves = False

if Product.Tabs.GetByName('Tine Heads').IsSelected == False:
    for a in Product.Attributes:
        for v in a.Values:
            if v.ValueCode == "9719" and v.IsSelected == True:
                allowSleves = True
                for attrs in Product.Tabs.GetByName('Tool Kit').Attributes:
                    for attrVal in attrs.Values:
                        if attrVal.ValueCode == '114-0590-01':
                            attrVal.IsSelected = True
        if allowSleves == False:
            for attr in Product.Tabs.GetByName('Sleves').Attributes:
                for attrValue in attr.Values:
                    attrValue.Allowed = False
        if allowSleves == False:
            for attrs in Product.Tabs.GetByName('Tool Kit').Attributes:
                for attrVal in attrs.Values:
                    attrVal.Allowed = False
                    Trace.Write(attrVal)

if Product.Tabs.GetByName('Tines').IsSelected == True:
    for attrs in Product.Tabs.GetByName('Tines').Attributes:
        for attrVal in attrs.Values:
            attrVal.Allowed = False
    for a in Product.Attributes:
        if a.Name == "Tine Heads":
            for v in a.Values:
                if v.ValueCode == "9719" and v.IsSelected == True:
                    allowSleves = True
                    for attrs in Product.Tabs.GetByName('Tool Kit').Attributes:
                        for attrVal in attrs.Values:
                            if attrVal.ValueCode == '114-0590-01':
                                attrVal.IsSelected = True
                if (v.ValueCode == "9719" and v.IsSelected) or (v.ValueCode == "9797" and v.IsSelected == True):
                    for attrs in Product.Tabs.GetByName('Tines').Attributes:
                        for attrVal in attrs.Values:
                            if attrVal.ValueCode == '78CoringTines':
                                Trace.Write('78CoringTines')
                                attrVal.Allowed = True
                            if attrVal.ValueCode == '78SolidTines':
                                attrVal.Allowed = True
                if (v.ValueCode == "9719" and v.IsSelected == True) or (v.ValueCode == "9796" and v.IsSelected == True) or (v.ValueCode == "9794" and v.IsSelected == True):
                    for attrs in Product.Tabs.GetByName('Tines').Attributes:
                        for attrVal in attrs.Values:
                            if attrVal.ValueCode == '34SolidTines':
                                Trace.Write('34SolidTines')
                                attrVal.Allowed = True
                            if attrVal.ValueCode == '34CoringTines':
                                attrVal.Allowed = True
                if v.ValueCode == "9739" and v.IsSelected == True:
                    for attrs in Product.Tabs.GetByName('Tines').Attributes:
                        for attrVal in attrs.Values:
                            if attrVal.ValueCode == '5mm8mmTines':
                                Trace.Write(attrVal.Allowed)
                                attrVal.Allowed = True
                if (v.ValueCode == "9736" and v.IsSelected == True) or (v.ValueCode == "9737" and v.IsSelected == True):
                    for attrs in Product.Tabs.GetByName('Tines').Attributes:
                        for attrVal in attrs.Values:
                            if attrVal.ValueCode == '38CoringTines':
                                attrVal.Allowed = True
                            if attrVal.ValueCode == '38SolidTines':
                                attrVal.Allowed = True