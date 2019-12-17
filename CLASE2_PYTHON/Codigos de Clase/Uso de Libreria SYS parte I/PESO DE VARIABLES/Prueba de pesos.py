import sys

a = list(range(10000))
b = tuple(a)

a1 = sys.getsizeof(a)
b1 = sys.getsizeof(b)

print ("PESO DE LA VARIABLE TIPO LISTA",a1,"BYTES")
print ("PESO DE LA VARIABLE TIPO TUPLA",b1,"BYTES")

input()