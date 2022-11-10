"""
Generacion de claves!
Script sencillo en python 3.9.2
Genera una clave mediante el ingreso de 3 frases del tamaño que necesites (minimo 16 caracteres entre las 3 frases)
Se suman todas las frases y se almacenan en una lista, la cual se divide por 16, el resultado es el espacio entre caracteres elegidos para que sea la clave
La longitud de la clave es de 16

"""

jmf = "fernandez"
jmf1="juanm"
jmf2= "@gmail.com"
print("*" * 20)
print("*" * 10)
print("*")
print("* Generacion de claves mediante frases.")
print("* Fernandez Juan Manuel")
print("*", jmf+jmf1+jmf2)
print("*")
print("*" * 20)
#frasex suma de frases
frasex=[]
# frase limpia de caracteres blancos
frasen=[]
# ingresos de frases
frase1 = str(input("Frase 1: "))
frase2 = str(input("Frase 2: "))
frase3 = str(input("Frase 3: "))

# sumatoria de frases en frasex
frasex += frase1 + frase2 + frase3
# Eliminamos todos los espacios en blanco, para guardar en una lista (frasen)
for stblancos in frasex:
    if stblancos != "" and stblancos != " ":
        frasen.append(stblancos)
# cantcar cantidad de caracteres en listas sin blancos
cantcar = len(frasen)
print("Cantidad de caracteres, eliminando los espacios en blanco: ", cantcar)
#lista con todos los caracteres
#print(frasen)
# si la suma de las frases tienen mas de 16 caracteres, podemos trabajar
if len(frasen) >= 16:
    # El resultado de la division sera la distancia entre caracteres, que seran parte de la clave
    div = (len(frasen) // 16)
    # varclave va a ir sumando de a 1 caracter en el for que sigue
    varclave = ""
    #print(div)
    sumocar = 0
    for i in frasen:
        sumocar += 1
        # 16 sera la longitud de la clave. De 0 a 15
        if sumocar == div and len(varclave) <= 15:
            varclave += i
            sumocar = 0
    print("Clave Generada: ", varclave)
else:
    print("La suma de las frases debe tener al menos 16 caracteres.")



# Ejemplo 1 (example 1)
#Frase 1: FrAse1 frase1 frase1
#Frase 2: frasE2frAse2 frase2
#Frase 3: frasE3 frAse3 frase3
# Resultado Clave: A1a1a1a2A2a2a3A3

# Ejemplo 2 (example 2)
# frase 1: Modificando un poco este bucle, puedes filtrar cualquier cosa de una lista, solo tienes que excluir lo que quieras. Por ejemplo, quiero que se eliminen todos los espacios en blanco y todos los vacíos
# Frase 2: El resultado es que hemos podido filtrar de manera automática los elementos que no están vacíos en una lista. Por supuesto, este bucle te sirve para listas de cualquier tamaño
# Frase 3: En este capítulo verás como eliminar los espacios vacíos de strings en lista de Python
# Resultado Clave: censeeldinuroesn
