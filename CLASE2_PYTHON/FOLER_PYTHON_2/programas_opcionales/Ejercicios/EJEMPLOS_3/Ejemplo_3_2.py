

texto = "en el amanecer al quinto dia"

vocales = "aeiou"

veces = 0

for i in texto:
	if i in vocales:
		veces += 1

print ("hay en total",veces,"vocales")			