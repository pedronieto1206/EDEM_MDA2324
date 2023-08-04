"""Module for Becoming Rich."""
import datetime
import random
import requests
from bs4 import BeautifulSoup

URL = "https://www.eduardolosilla.es/quiniela/ayudas/proximas"

page = requests.get(URL, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")


def parse_match(match):
    """Function parsing match"""
    part = {}
    part["local"] = match.split("-")[0]
    part["visitante"] = match.split("-")[1]
    return part


def calculate_quiniela(qui):
    """Function parsing quiniela"""
    for part in qui:
        part["resultado"] = random.choice(["1", "X", "2"])
        qui[qui.index(part)] = part
    return qui


elements = soup.find_all(
    "div", {"class": "c-ayudas-proximas__tabla-partidos ng-star-inserted"})

for element in elements:
    quiniela = []
    jornada = element.find_all(
        "div", {"class": "c-ayudas-proximas__tabla-partidos__titulo"})[0].text
    fecha = jornada.split("-")[1].replace(" ", "")
    date_time_obj = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    if date_time_obj < datetime.datetime.now() + datetime.timedelta(days=7):
        print("###############################################")
        print(jornada)
        print("###############################################")
        partidos = element.find_all(
            "span", {"class": "c-equipos__teams m-short ng-star-inserted"})
        pleno = element.find_all(
            "span", {"class": "c-equipos__teams ng-star-inserted"})
        pleno.text = pleno[0].text.replace(" ", "").replace("\n", "-")[1:-1]
        partidos.append(pleno)
        for partido in partidos:
            quiniela.append(
                parse_match(partido.text.replace(" ", "").replace("\n", "")))
        quiniela = calculate_quiniela(quiniela)
        print(f'{"LOCAL":<20} {"VISITANTE":<20} {"RESULTADO":<10}')
        for element in quiniela:
            local, visitante, resultado = element.values()
            print(f'{local:<20} {visitante:<20} {resultado:<10}')
