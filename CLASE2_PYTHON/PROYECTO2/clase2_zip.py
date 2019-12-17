import time
#hacer uso de la función zip y range
l1=[0,2,4] #[0 2 4]
#built-in functions
maximo=max(l1)
minimo=min(l1)
suma=sum(l1)
print(maximo,minimo,suma)
r1=range(3) # 0 1 2
t1=("hola","buenos","dias","labotec")
#comprimir dos elementos iterables
z1=zip(l1,r1,t1)
for val_l,val_r,val_T in z1:
    print(val_l,val_r,val_T)
    time.sleep(1)