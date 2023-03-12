def printclr(str, c, stl='n'):
    styles = {
        "n": "00",
        "b": "01",
        "i": "03",
        "ul": "04"
    }
    colors = {
        "negro": f"\033[{styles[stl]};30m",
        "rojo": f"\033[{styles[stl]};31m",
        "verde": f"\033[{styles[stl]};32m",
        "amarillo": f"\033[{styles[stl]};33m",
        "azul": f"\033[{styles[stl]};34m",
        "magenta": f"\033[{styles[stl]};35m",
        "cyan": f"\033[{styles[stl]};36m",
        "gris_claro": f"\033[{styles[stl]};37m",
        "gris": f"\033[{styles[stl]};90m",
        "rojo_claro": f"\033[{styles[stl]};91m",
        "verde_claro": f"\033[{styles[stl]};92m",
        "amarillo_claro": f"\033[{styles[stl]};93m",
        "azul_claro": f"\033[{styles[stl]};94m",
        "magenta_claro": f"\033[{styles[stl]};95m",
        "cyan_claro": f"\033[{styles[stl]};96m",
        "blanco": f"\033[{styles[stl]};97m",
        "f_negro": f"\033[{styles[stl]};40m",
        "f_rojo": f"\033[{styles[stl]};41m",
        "f_verde": f"\033[{styles[stl]};42m",
        "f_amarillo": f"\033[{styles[stl]};43m",
        "f_azul": f"\033[{styles[stl]};44m",
        "f_magenta": f"\033[{styles[stl]};45m",
        "f_cyan": f"\033[{styles[stl]};46m",
        "f_gris_claro": f"\033[{styles[stl]};47m",
        "f_gris": f"\033[{styles[stl]};100m",
        "f_rojo_claro": f"\033[{styles[stl]};101m",
        "f_verde_claro": f"\033[{styles[stl]};102m",
        "f_amarillo_claro": f"\033[{styles[stl]};103m",
        "f_azul_claro": f"\033[{styles[stl]};104m",
        "f_magenta_claro": f"\033[{styles[stl]};105m",
        "f_cyan_claro": f"\033[{styles[stl]};106m",
        "f_blanco": f"\033[{styles[stl]};107m"
    }
    fin = "\033[00m"
    print( f"{colors[c]}{str}{fin}" )

# tuplas
printclr("-- ------------ Pruebas con tuplas ------------", "verde")
tupla = (1, 8, [ 'uno', 'dos' ])
# tupla[1] = 55; # TypeError: 'tuple' object does not support item assignment
tupla[2][0] = 'uno-test';
print(tupla)

# Numpy arrays
printclr("-- ------------ Pruebas con npArrays ------------", "verde")
import numpy as np

array = np.array([1, 5, 8])
res = array + 1

array = np.array(['uno', 'dos', 'tres'])
# res = array + '-test'
def concat(array, str):
    na = []
    for i in range(len(array)):
        na.append(f"{array[i]}{str}")
    return np.array(na)

newArray = concat(array, '|test')
for item in newArray:
    print(item)



# DataFrames con lambda functions
printclr("-- ------------ DataFrames con lambda functions ------------", "verde")
import pandas as pd

diccionario = {
    "cuno": [1, 87, 3, 94, 65, 25],
    "cdos": [9, 5, 85, 34, 5, 6]
}
df = pd.DataFrame(diccionario)
print( df.head(2) )
df["cuno"] = df.apply( lambda x: x["cuno"]+2, axis=1 )
print( df.head(2) )
df["ctre"] = df.apply( lambda x: x["cuno"]+2, axis=1 )
print( df.head(2) )




# Series de panda
printclr("-- ------------ Series de un DataFrame de pandas ------------", "verde")

diccionario = {
    "cuno": ["uno.test", "dos.test", "tre.test"],
    "cdos": ["cua.test", "cin.test", "sei.test"]
}
df = pd.DataFrame(diccionario)
df["res"] = df["cuno"].str.replace(".","-", regex=True)