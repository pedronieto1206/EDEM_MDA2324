# EDEM_MDA2324

<div align="center"><img src="https://www.hollywoodreporter.com/wp-content/uploads/2018/09/simpsons_header-h_2018.jpg?w=1024"  width="350px" height="250px" alt="Simpsons Challenge" /></div>

Este ejercicio tiene como objetivo que el alumno se familiarice con el uso de la herramienta de control de versiones Git y con la plataforma GitHub, además de utilizar los conocimientos adquiridos hasta el momento sobre el uso de la consola de Linux, python, docker y contenedores.

Este ejercicios se divide en tres niveles:

## Nivel Maggie

<div align="center"><img src="https://upload.wikimedia.org/wikipedia/en/9/9d/Maggie_Simpson.png"  width="150px" height="250px" alt="Simpsons Challenge" /></div>

- Usando google colab crear un notebook que consuma la api de los simpsons y haga una consulta cada 30seg a la API
- El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).
- Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de manera autónoma. El Docker debe tener el código en una carpeta app
- El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger citas de ellos dos.


## Nivel Lisa

<div align="center"><img src="https://upload.wikimedia.org/wikipedia/bs/thumb/e/ec/Lisa_Simpson.png/220px-Lisa_Simpson.png"  width="150px" height="250px" alt="Simpsons Challenge" /></div>

- Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del mismo.
- El código debe mantener un diccionario de palabras y escribir en cada iteración en un fichero el conteo de palabras que lleva.

    The;1
    Great;2

- El código debe crear de manera dinámica las carpetas con nuevos personajes

## Nivel Bart

<div align="center"><img src="https://static.simpsonswiki.com/images/thumb/6/65/Bart_Simpson.png/200px-Bart_Simpson.png"  width="150px" height="250px" alt="Simpsons Challenge" /></div>

- Construid un Docker-compose con una imagen de un contenedor de Jupyter
- Dentro del Jupyter generad un notebook con una gráfica mostrando las palabras más habituales en las quotes
- Mostrar un listado de las carpetas y las fotos de los personajes en el jupyter
- Docker-compose debe ser capaz de hacer build del contenedor original
