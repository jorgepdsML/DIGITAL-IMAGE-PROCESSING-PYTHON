import ast,os,time

entrada = input("Ingrese la lista de numeros: ")
a = ast.literal_eval(entrada)
b = len(a)-1

while (b!=0):
	for i in range (0,b):
		if a[i]>a[i+1]:
			a[i],a[i+1] = a[i+1],a[i]
			os.system("cls")
			print (a)
			time.sleep(1)
	b = b-1   

os.system("cls")

print ("finalizado!\nEl resultado es: {}".format(a))    
input()