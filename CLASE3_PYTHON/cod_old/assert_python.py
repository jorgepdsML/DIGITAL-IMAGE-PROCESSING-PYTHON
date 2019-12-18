#funcion assert
x1=0
try:
    assert(x1==0)
    N1=input ("ingresar altura")
    N1=int(N1)
    N2= input("ingresar  base")
    N2=int(N2)
    
    for i in range(N1):
       
     
        for j in range(N2):
            
            print("*",end=' ')
        print("\n")   
except AssertionError:
    print("SE EJECUTO UN ERROR")
except ValueError:
    print("Error por valor")
 
