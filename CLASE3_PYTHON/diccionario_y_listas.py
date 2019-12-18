#crear una base de datos mediante el uso de diccionarios y listas
base_de_datos={"temperatura":[],"humedad":[]  }
print("base de datos al inicio",base_de_datos)
#acceder al campo temperatura y humedad para agregarle 3 elementos
base_de_datos["temperatura"].append(40)
base_de_datos["temperatura"].append(20)
base_de_datos["temperatura"].append(30)
#para humedad
base_de_datos["humedad"].append(50)
base_de_datos["humedad"].append(40)
base_de_datos["humedad"].append(45)
print("base de datos al final",base_de_datos)