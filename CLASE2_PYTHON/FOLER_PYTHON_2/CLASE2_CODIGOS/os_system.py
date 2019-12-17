import os
import time
p=input("¿que archivo deseas abrir ?")
if p=="lista_media_var":
    p=p+".py"
    #hacer uso de comandos del terminal
    os.system(p)
else:
    print("no disponible")
