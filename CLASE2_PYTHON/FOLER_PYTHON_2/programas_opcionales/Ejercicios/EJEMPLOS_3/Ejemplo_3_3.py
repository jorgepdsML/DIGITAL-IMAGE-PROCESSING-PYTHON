

texto = input("Ingrese una palabra: ")

for i in range(len(texto)):
	if not(texto[i]==texto[-i-1]):
		print ("La palabra no es identica en modo inverso a si misma!")
		break
	if i== len(texto)-1:
		print ("La palabra si es identica en modo inverso a si misma!")

input()
		