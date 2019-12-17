#Temperaturas en Celsius:
x = [23,18,19,24.5,20.18,20,17.32]

# K = C + 273.15
#######################################
for i in range(len(x)):
	x[i] = x[i] + 273.15
#######################################
x2 = []
for i in range(len(x)):
	x2.append(x[i]+273.15)
#######################################
x3 = list(map(lambda x:round(x+273.15,2),x))
print(x3)
