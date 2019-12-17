x=[-10,12,20,30]
y=list()
#realizar un recorrido sobre la lista x
for it in x:
    if it>=0:
        y.append(it)
    else:
        y.append(0)
print(x,y)
    
