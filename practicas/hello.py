
"""
Esta es mi primera prueba imprimiendo
"""
print("Hola mundo")
print(125)

# Variables
texto = "Mi texto"
texto2 = 'Otro texto con otras comillas'
numero = 7954
numero2 = 77

# Concatenando
print(f"{texto} - {str(numero)}")
print(f"{texto2} - {numero2}")
print(texto +" - "+ texto2)

# Entrada de datos
nombre = input("Cual es tu nombre?: ")
print(f"Hola {nombre}, que tal?")

# Condiciones
altura = int(input("Cuan alto eres?: "))
if altura >= 180:
    print("Eres alto")
else:
    print("Eres bajo")

# Funciones

nacionalidad = input("Eres venezolano?: ")
def getNacionalidad(n):
    resultado = "No se si te gustan las arepas"
    if n == "si":
        resultado = "Seguro que te gustan las arepas"
    
    return resultado

nacionalidad = getNacionalidad(nacionalidad)
print(nacionalidad)

# Listas
personas = [ "Hisham", "sharif", "Faisal" ]

# Bucles
for p in personas:
    print(f"-{p}")

print( ", ".join(personas) )
separador = ", "
print( separador.join(personas) )