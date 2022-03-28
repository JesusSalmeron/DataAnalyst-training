import pandas as pd



diccionario = {
    "Nombre":["Juan","Jesus","Maria"],
    "edad":[20,23,25],
    "dni":["766533535A","645455478A","255515129V"]
}
df = pd.DataFrame(diccionario)

# 1
df["profesiones"] = ["Ingeniero","Abogazo","Juez"]
print(df)


# 2
df = df.assign(sueldo=[2000,563,4500])
print(df)


# 3
df.insert(3,"Enail",["pepito@hotmai","fulanito@algo","saulGoodman@BB"])
print(df)
