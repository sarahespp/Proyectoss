# CineMatch - Avance 2
# Operadores que se usaran durante todo el proyecto

print("Bienvenido a CineMatch!")
print("Encuentra una pelicula de acuerdo con tus preferencias.")

# Menu para que el usuario escoja sus preferencias
print("Generos:")
print("1. Accion")
print("2. Comedia")
print("3. Romance")
print("4. Suspenso")
print("5. Ciencia ficcion")
print("6. Animacion")

genero_escogido = int(input("Selecciona un genero (1 al 6): "))

print("Duracion:")
print("1. Corta (menos de 90 minutos)")
print("2. Media (de 90 a 120 minutos)")
print("3. Larga (mas de 120 minutos)")

duracion_escogida = int(input("Selecciona una duracion (1 al 3): "))
calificacion_minima = float(input("Indica la calificacion minima que buscas (0 a 10): "))

# Ejemplo datos de  pelicula
nombre_pelicula = "Interestelar"
genero_pelicula = 5
duracion_pelicula = 169
calificacion_pelicula = 8.7

# Convertir duracion de minutos a duracion horas y minutos
# Esta operacion nos servira en proximos avances
duracion_en_horas = duracion_pelicula // 60
minutos_restantes = duracion_pelicula % 60

# Comparaciones que despues se utilizaran en decisiones (if)
genero_coincide = genero_escogido == genero_pelicula
calificacion_coincide = calificacion_pelicula >= calificacion_minima

# Clasificar la duración real de Interestelar en corta, media o larga
pelicula_corta = duracion_pelicula < 90
pelicula_media = duracion_pelicula >= 90 and duracion_pelicula <= 120
pelicula_larga = duracion_pelicula > 120

# En avances posteriores se agregarán decisiones para determinar
# si la película coincide completamente con las preferencias del usuario.
# También se incluirán muchas más películas en un catálogo para recomendar varias opciones.


print("--- Pelicula encontrada ---")
print("Nombre:", nombre_pelicula)
print("Duracion:", duracion_en_horas, "horas y", minutos_restantes, "minutos")
print("Calificacion:", calificacion_pelicula)

print("--- Resultado de las comparaciones ---")
print("Tu buscabas el genero:", genero_escogido)
print("¿Coincide el genero?", genero_coincide)
print("Tu buscabas la calificacion minima:", calificacion_minima)
print("¿Cumple la calificacion minima?", calificacion_coincide)
print("Tu buscabas la duracion:", duracion_escogida)
print("¿Es una pelicula de duracion corta?", pelicula_corta)
print("¿Es una pelicula de duracion media?", pelicula_media)
print("¿Es una pelicula larga?", pelicula_larga)
