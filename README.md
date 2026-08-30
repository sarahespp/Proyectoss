# Proyecto CineMatch
Repositorio para "Fundamentos de programacion" agosto-diciembre 2026

Tema del proyecto: Recomendador de películas CineMatch

El proyecto consiste en desarrollar un programa que permita a los usuarios encontrar recomendaciones de películas de acuerdo con sus gustos y preferencias. El programa le dará al usuario diferentes opciones como género, duración y calificación para escoger, y al final le arrojará la película que más se ajuste a sus preferencias.

¿Por qué es interesante?
Elegí este proyecto porque me gustan mucho las películas al igual que muchas personas, pero a veces puede ser difícil decidir qué película ver entre tantas opciones. Es por eso que me parece interesante crear una herramienta que utilice información proporcionada por el usuario para ayudarlo a encontrar una película que se adapte a sus preferencias. 

ALGORITMO

Entradas

Opción de género: 1, 2, 3, 4, 5, 6 

Opción de duración: 1, 2, 3

Opción de calificación: 1, 2, 3

Opción para realizar otra búsqueda: "sí" o "no"


Proceso


1.INICIO

2.MOSTRAR el nombre y la explicación del programa.

3.MOSTRAR las 6 opciones de género.

4.PEDIR al usuario que seleccione un género del 1 al 6.

5.GUARDAR la selección en la variable género.

6.MOSTRAR las 3 opciones de duración.

7.PEDIR al usuario que seleccione una duración.

8.GUARDAR la selección en la variable duración.

9.MOSTRAR las 3 opciones de calificación.

10.PEDIR al usuario que seleccione una calificación mínima.

11.GUARDAR la selección en la variable calificación.

12.BUSCAR películas que coincidan exactamente con género, duración y calificación.

13.SI existen coincidencias exactas:

 13.1. MOSTRAR las películas encontradas.
 
 13.2. MOSTRAR la información de cada película.
 
14.SI NO existen coincidencias exactas:

 14.1. BUSCAR películas que coincidan con género y calificación, permitiendo una diferencia en la duración.
 
15.SI existen coincidencias con duración similar:

 15.1. MOSTRAR un mensaje indicando que no hay coincidencias exactas, pero existen películas similares.
 
 15.2. MOSTRAR las películas encontradas.
 
16.SI NO existen coincidencias con duración similar:

 16.1. BUSCAR películas que coincidan con género y duración, permitiendo una diferencia en la calificación.
 
17.SI existen coincidencias con calificación similar:

 17.1. MOSTRAR un mensaje indicando que no hay coincidencias exactas, pero existen películas con una calificación similar.
 
 17.2. MOSTRAR las películas encontradas.
 
18.SI NO existen coincidencias con calificación similar:

 18.1. MOSTRAR un mensaje indicando que no se encontraron películas adecuadas dentro de las preferencias seleccionadas.
 
19.PREGUNTAR al usuario si desea realizar otra búsqueda.

20.SI responde "sí":

 20.1. REPETIR el proceso desde el paso 2.
 
21.SI responde "no":

 21.1. MOSTRAR un mensaje de despedida.
 
22.FIN

Salidas

Películas recomendadas.

Información de las películas recomendadas.

Mensaje cuando existen coincidencias parciales.

Mensaje cuando no se encuentran películas adecuadas dentro del género seleccionado.

Mensaje de despedida.
