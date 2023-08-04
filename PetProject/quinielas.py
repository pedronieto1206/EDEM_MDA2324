import requests
import json
from bs4 import BeautifulSoup
import datetime
import random


URL = "https://www.eduardolosilla.es/quiniela/ayudas/proximas"


page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

def parse_match(match):
    partidos={}
    partidos["local"]=match.split("-")[0]
    partidos["visitante"]=match.split("-")[1]
    return partidos

def calculate_quiniela(quiniela):
    for partido in quiniela:
        partido["resultado"]=random.choice(["1","X","2"])
        quiniela[quiniela.index(partido)]=partido
    return quiniela


elements=soup.find_all("div", {"class": "c-ayudas-proximas__tabla-partidos ng-star-inserted"})

for element in elements:
    quiniela=[]
    jornada=element.find_all("div", {"class": "c-ayudas-proximas__tabla-partidos__titulo"})[0].text
    fecha=jornada.split("-")[1].replace(" ","")
    date_time_obj = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    if date_time_obj < datetime.datetime.now() + datetime.timedelta(days=7):
        print("###############################################")
        print(jornada)
        print("###############################################")
        partidos=element.find_all("span", {"class": "c-equipos__teams m-short ng-star-inserted"})
        pleno=element.find_all("span", {"class": "c-equipos__teams ng-star-inserted"})
        pleno.text=(pleno[0].text.replace(" ","").replace("\n","-")[1:-1])
        partidos.append(pleno)
        for partido in partidos:
            quiniela.append(parse_match(partido.text.replace(" ","").replace("\n","")))
        quiniela=calculate_quiniela(quiniela)
        print("{:<20} {:<20} {:<10}".format('LOCAL', 'VISITANTE', 'RESULTADO'))
        for element in quiniela:
            local, visitante, resultado = element.values()
            print("{:<20} {:<20} {:<10}".format(local, visitante, resultado))






