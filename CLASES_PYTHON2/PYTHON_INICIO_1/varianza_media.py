"""
CALCULO DE LA MEDIA Y LA VARIANZA
"""
x=[10,20,30,40]
#media
u=sum(x)/len(x)
#varianza
var=0
for v in x:
    var+=(v-u)**2
var=(var/len(x))

print("MEDIA ES IGUAL A ;",u)
print("VARIANZA ES IGUAL A :",var)

