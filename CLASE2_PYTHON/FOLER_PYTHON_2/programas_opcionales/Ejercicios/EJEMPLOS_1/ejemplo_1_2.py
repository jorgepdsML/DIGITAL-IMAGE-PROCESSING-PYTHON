#Como no sabemos cuantos cubos perfectos  existen
#entre '1000' y '10000', entonces usamos un bucle
#'while' tal que se mantenga  en  esta  condicion
#hasta que detecte que se ha excedido  el  numero
#maximo indicado (empezaremos  a  analizar  desde
#el numero '0').

#Numero base:
numero_base = 0

#Bucle 'while'
while (numero_base**3 < 10000):
	if 1000<=numero_base**3<=10000:
		print (numero_base**3)
	numero_base += 1 

#Pausa esperando por un enter para cerrar la consola.
input()
			
'''
NOTA:
Analizarlo con un bucle 'for', sacandole la raiz cubica
a los extremos para saber los limites no  es  algo  muy
preciso en estos casos ya que no hay  forma  exacta  de
ingresar '1/3' para extraer la raiz cubica de un numero.
'''	
	