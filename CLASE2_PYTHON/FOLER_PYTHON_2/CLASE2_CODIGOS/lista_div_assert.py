#definir una función que reciba 2 listas como argumento y retornar la division
#elemento a elemento
def div_list(l1,l2):
    N1=len(l1)
    N2=len(l2)
    #definir una lista
    lista_div=list()
    #realizar recorrido sobre ambas listas
    for num,den in zip(l1,l2):
         assert(den!=0)
         lista_div.append(num/den)
    return lista_div

l1=div_list([10,5],[0,1])
print(l1)

    
        

    
