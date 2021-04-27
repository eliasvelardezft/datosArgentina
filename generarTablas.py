import json
import pyodbc
import requests
# Eliminar esta linea, en mi caso es para importar los datos del servidor y la db.
import SECRETS

# En las siguientes lineas va la información del servidor y la db donde se quieran crear las tablas
server = SECRETS.server
database = SECRETS.database
username = SECRETS.username
password = SECRETS.password

provincias = requests.get('https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.2/download/provincias.json').json()
departamentos = requests.get('https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.3/download/departamentos.json').json()
localidades = requests.get('https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.27/download/localidades-censales.json').json()


# Creación tabla provincias
crearTablaProvincias = '''DROP TABLE IF EXISTS Provincias;
CREATE TABLE Provincias (
  id int NOT NULL,
  nombre varchar(255) NOT NULL,
  PRIMARY KEY (id)
)'''
cursor.execute(crearTablaProvincias)


# For loop para hacer insert de cada provincia
for provincia in provincias['provincias']:
    nombre = provincia['nombre']
    id = provincia['id']
    print(f'id: {id}, nombre: {nombre}')
    query = 'INSERT INTO dbo.Provincias (id, nombre) VALUES (?, ?)'
    data = [(id, nombre)]
    cursor.executemany(query, data)
    cursor.commit()


# Creación tabla departamentos
crearTablaDepartamentos = '''DROP TABLE IF EXISTS Departamentos;
CREATE TABLE Departamentos (
  id int NOT NULL,
  nombre varchar(255) NOT NULL,
  id_provincia int FOREIGN KEY REFERENCES Provincias(id),
  PRIMARY KEY (id)
)'''
cursor.execute(crearTablaDepartamentos)

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


# Creación tabla localidades
crearTablaLocalidades = '''DROP TABLE IF EXISTS Localidades;
CREATE TABLE Localidades (
  id int NOT NULL,
  nombre varchar(255) NOT NULL,
  id_departamento int FOREIGN KEY REFERENCES Departamentos(id),
  PRIMARY KEY (id)
)'''
cursor.execute(crearTablaLocalidades)

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
