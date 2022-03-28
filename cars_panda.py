import pandas as pd


# Método 1

columnas = ["marca","precio","disponibilidad"]
cocheA = ["Audi",20000,True]
cocheB = ["Mercedes",15000,False]

df = pd.DataFrame([cocheA,cocheB],columns = columnas)
print(df)
print("")

# Método 2

marcas = [
    "Seat",
    "bmw",
    "Renault"
]

precios = [
    20000,
    15000,
    3000
]

disponible = [
    True,
    True,
    False
]

df = pd.DataFrame(list(zip(marcas,precios,disponible)),columns = ["marca","precio","disponibilidad"])
print(df)

# Método 3

marcas = [
    "Subaru",
    "Ferrari",
    "Renault"
]

precios = [
    20000,
    15000,
    3000
]

disponible = [
    True,
    True,
    False
]


diccionario = {
    "marcas" : marcas,
    "precios" : precios,
    "disponible" : disponible
}

df = pd.DataFrame(diccionario)
print("")
print(df)
