import pandas as pd
import requests 
from bs4 import BeautifulSoup


url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Equipos:

teams = soup.find_all('span',class_="nombre-equipo")  #<span itemprop="name" class="nombre-equipo">Real Madrid</span>

equipos = []

count = 0
for i in teams:
    if count < 20:
        equipos.append(i.text)
    else:
        break

    count +=1

# Puntos:

pt = soup.find_all('td',class_="destacado")  

puntos = []

count = 0
for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count +=1


df = pd.DataFrame({'Nombre: ':equipos, 'Puntos: ':puntos}, index=list(range(1,21)))
df.to_csv('Clasificación.csv')
