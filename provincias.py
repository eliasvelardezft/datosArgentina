import json
import pyodbc
import requests
import SECRETS

server = SECRETS.server
database = SECRETS.database
username = SECRETS.username
password = SECRETS.password
con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = con.cursor()

provincias = requests.get('https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.2/download/provincias.json').json()
departamentos = requests.get('https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.3/download/departamentos.json').json()
localidades = requests.get('https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.27/download/localidades-censales.json').json()


# For loop para hacer insert de cada provincia
for provincia in provincias['provincias']:
    nombre = provincia['nombre']
    id = provincia['id']
    print(f'id: {id}, nombre: {nombre}')
    query = 'INSERT INTO dbo.Provincias (id, nombre) VALUES (?, ?)'
    data = [(id, nombre)]
    cursor.executemany(query, data)
    cursor.commit()

# For loop para hacer insert de cada Departamento
for departamento in departamentos['departamentos']:
    nombre = departamento['nombre']
    id = departamento['id']
    id_provincia = departamento['provincia']['id']
    print(f'id: {id}, nombre: {nombre}, id_provincia: {id_provincia}')
    query = 'INSERT INTO dbo.Departamentos (id, nombre, id_provincia) VALUES (?, ?, ?)'
    data = [(id, nombre, id_provincia)]
    cursor.executemany(query, data)
    cursor.commit()

# For loop para hacer insert de cada Localidad
for localidad in localidades['localidades-censales']:
    nombre = localidad['nombre']
    id = localidad['id']
    id_departamento = localidad['departamento']['id']
    print(f'id: {id}, nombre: {nombre}, id_departamento: {id_departamento}')
    query = 'INSERT INTO dbo.Localidades (id, nombre, id_departamento) VALUES (?, ?, ?)'
    data = [(id, nombre, id_departamento)]
    cursor.executemany(query, data)
    cursor.commit()

    