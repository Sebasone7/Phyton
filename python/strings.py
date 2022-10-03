myStr = "hallo world"

print(dir(myStr))    
print(myStr.upper()) #la funcion .upper() convierte el de min a MAYUS

print(myStr.count("a")) #cuenta el caracter a

print(myStr.replace("cbaxal","boss").upper()) #encadenado


print(myStr.startswith("cbaxal")) #true and false


print(myStr.split()) #separa el texto

print(myStr.find("h")) #imprime la posicion en donde se encuentra la letra h
print(len(myStr))# longituud del texto comienza desde 1

print(myStr.index(("a"))) #indica la posicion comenzando desde cero
print(myStr.isnumeric()) #pregunta si es numerico

print(myStr.isalpha()) #pregunta si es alfabetico

print(myStr[4]) #muestra la posicion 4 del texto

print(myStr[-1]) #muestra la posicion -1 es decir se devuelve
