# datosArgentina
Creación de tablas "Provincias", "Departamentos" y "Localidades" en una base de datos SQL server con Pyodbc

El script fue generado con python 3 y crea (las dropea si existen previamente) las tablas 'Provincias', 'Departamentos' y 'Localidades', así como también las relaciones de FK entre ellas en una base de datos SQL Server utilizando la librería Pyodbc.

Los datos son tomados de un JSON provisto por el gobierno.

En la sección luego de los imports deben especificarse los datos del servidor y db donde se quieran crear las tablas.

Nota: la localidad 'Ciudad Autónoma de Buenos Aires' no está ligada a ningún departamento (FK NULL) ya que así se encuentra en el JSON del gobierno. En el JSON esta localidad esta ligada a la Provincia 'Ciudad Autónoma de Buenos Aires', pero en las tablas generadas no existe esa relación.

# Requerimientos
* Python 3
* Microsoft ODBC driver 17
* Pyodcb (Version utilizada: 4.0.30)
