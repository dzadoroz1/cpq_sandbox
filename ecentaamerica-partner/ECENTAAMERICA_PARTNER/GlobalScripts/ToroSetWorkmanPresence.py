contains_workman = 'No'
for item in context.Quote.GetAllItems():
    if item.CategoryId == 119:
        contains_workman = 'Yes'
        break
        
context.Quote['Toro_Contains_Reelmaster'] = contains_workman