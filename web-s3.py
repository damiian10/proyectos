
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("./chromedriver.exe")

ids=[] #ID de la tabla de estudiantes
apellidos=[] #apellidos de la tabla de estudiantes
nombres=[] #nombres de la tabla de estudiantes
generos=[] #genreros de la tabla de estudiantes
emails=[] #emails de la tabla de estudiantes
ciudades=[] #ciudades de la tabla de estudiantes
materias=[] #materias de la tabla de estudiantes
aulas=[] #aulas de la tabla de estudiantes
semestres=[] #semestres de la tabla de estudiantes
modalidades=[] #modalidades de la tabla de estudiantes
niveles=[] #niveles de la tabla de estudiantes
tutores=[] #tutores de la tabla de estudiantes
titulos=[] #titulos de la tabla de estudiantes
emailstutores=[] #emials tutores de la tabla de estudiantes



driver.get("http://127.0.0.1:8000/")

#r = requests.get('http://127.0.0.1:8000/')
content = driver.page_source
soup = BeautifulSoup(content)

cursos = soup.find('div' , class_= "table-responsive" )

for curso in cursos.find_all('tbody'):
    rows = curso.find_all('tr')
    for row in rows:
        sap = row.find('td', class_= 'standing-table__cell standing-table__cell--name')
        id1= row.find_all('td')[0].text
        apellido1 = row.find_all('td')[1].text
        nombre1 = row.find_all('td')[2].text
        genero1 = row.find_all('td')[3].text
        email1 = row.find_all('td')[4].text
        ciudad1 = row.find_all('td')[5].text
        materia1 = row.find_all('td')[6].text
        aula1 = row.find_all('td')[7].text
        semestre1 = row.find_all('td')[8].text
        modalidad1 = row.find_all('td')[9].text
        nivel1 = row.find_all('td')[10].text
        tutor1 = row.find_all('td')[11].text
        titulo1 = row.find_all('td')[12].text
        emailtutor1 = row.find_all('td')[13].text
        #print(pl_team, apellidos)
        ids.append(id1)
        apellidos.append(apellido1)
        nombres.append(nombre1)
        generos.append(genero1)
        emails.append(email1)
        ciudades.append(ciudad1)
        materias.append(materia1)
        aulas.append(aula1)
        semestres.append(semestre1)
        modalidades.append(modalidad1)
        niveles.append(nivel1)
        tutores.append(tutor1)
        titulos.append(titulo1)
        emailstutores.append(emailtutor1)

for id in ids:
    print(id)

for apellido in apellidos:
    print(apellido)

for nombre in nombres:
    print(nombre)

for genero in generos:
    print(genero)

for email in emails:
    print(email)

for ciudad in ciudades:
    print(ciudad)

for materia in materias:
    print(materia)

for aula in aulas:
    print(aula)

for semestre in semestres:
    print(semestre)

for modalidad in modalidades:
    print(modalidad)

for nivel in niveles:
    print(nivel)

for tutor in tutores:
    print(tutor)

for titulo in titulos:
    print(titulo)

for emailtutor in emailstutores:
    print(emailtutor)

#df = pd.DataFrame({'ID':ids,'APELLIDO': apellidos,'NOMBRE':nombres,'GENERO':generos, 'EMAIL ESTUDIANTE':emails, 'CIUDAD':ciudades, 'MATERIA':materias ,'AULA':aulas ,'SEMESTRE':semestres, 'MODALIDAD':modalidades, 'NIVEL':niveles, 'TUTOR ASIGNADO':tutores,'TITULO':titulos, 'EMAIL TUTOR':emailstutores })
#df.to_csv('SISTEMA DE INSCRIPCION DE ESTUDIANTES.csv', index=False, encoding='utf-8')