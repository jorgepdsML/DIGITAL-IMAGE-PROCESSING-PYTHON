x = [12,13,7,18,22,33,9,10,17]


y = []
for i in range(len(x)):
	if x[i]<15:
		y.append(x[i])

x2 = list(filter(lambda x:x<15,x))
print (x2)