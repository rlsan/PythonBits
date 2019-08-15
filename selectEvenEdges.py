from pymel.all import *
selectionArray = []
i = 0

for each in selected(fl = True):
    
    if  i % 2 == 0 :
        selectionArray.append(each)    
    i +=1

print selectionArray 
select (selectionArray )    