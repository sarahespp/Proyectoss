# CineMatch Avance 4
# Estructuras de decisión

# Función que muestra el mensaje de bienvenida al usuario
def mostrar_bienvenida():
    print("Bienvenido a CineMatch!")
    print("Encuentra una pelicula de acuerdo con tus preferencias.")

# Función que muestra las opciones de género y guarda la opción seleccionada por el usuario
def pedir_genero():
    print("\nGeneros:")
    print("1. Accion")
    print("2. Comedia")
    print("3. Romance")
    print("4. Suspenso")
    print("5. Ciencia ficcion")
    print("6. Animacion")

    genero_escogido = int(input("Selecciona un genero (1 al 6): "))
    return genero_escogido

# Función que muestra las opciones de duración y guarda la opción seleccionada por el usuario
def pedir_duracion():
    print("\nDuracion:")
    print("1. Corta (menos de 90 minutos)")
    print("2. Media (de 90 a 120 minutos)")
    print("3. Larga (mas de 120 minutos)")

    duracion_escogida = int(input("Selecciona una duracion (1 al 3): "))
    return duracion_escogida

# Función que pide y guarda la calificación mínima que busca el usuario
def pedir_calificacion():
    calificacion_minima = float(input("Indica la calificacion minima que buscas (0 a 10): "))
    return calificacion_minima

# Función que convierte la duración de una película de minutos a horas
def calcular_horas(duracion_pelicula):
    horas = duracion_pelicula // 60
    return horas

# Función que calcula los minutos que sobran después de convertir la duración a horas
def calcular_minutos_restantes(duracion_pelicula):
    minutos = duracion_pelicula % 60
    return minutos

# Función que muestra en pantalla los datos de la película
def mostrar_pelicula(nombre_pelicula, duracion_pelicula, calificacion_pelicula):
    horas = calcular_horas(duracion_pelicula)
    minutos = calcular_minutos_restantes(duracion_pelicula)

    print("\n--- Pelicula encontrada ---")
    print("Nombre:", nombre_pelicula)
    print(f"Duracion: {horas} horas y {minutos} minutos")
    print("Calificacion:", calificacion_pelicula)

# Función que compara el género que busca el usuario con el género de la película
def comparar_genero(genero_escogido, genero_pelicula):
    return genero_escogido == genero_pelicula

# Función que compara la calificación de la película con la calificación mínima que busca el usuario
def comparar_calificacion(calificacion_pelicula, calificacion_minima):
    return calificacion_pelicula >= calificacion_minima

# Función que compara la duración que busca el usuario con la duración de la película
def comparar_duracion(duracion_escogida, duracion_pelicula):
    if duracion_escogida == 1:
        return duracion_pelicula < 90
    elif duracion_escogida == 2:
        return 90 <= duracion_pelicula <= 120
    elif duracion_escogida == 3:
        return duracion_pelicula > 120
    else:
        return False
    
# Función que decide si la película coincide con las preferencias del usuario
def decidir_recomendacion(genero_coincide, duracion_coincide, calificacion_coincide):
    if genero_coincide and duracion_coincide and calificacion_coincide:
        return True
    else:
        return False

# Programa principal
# Se ejecutan las funciones para obtener las preferencias del usuario
mostrar_bienvenida()
genero_escogido = pedir_genero()
duracion_escogida = pedir_duracion()
calificacion_minima = pedir_calificacion()

# Datos de una película de ejemplo
nombre_pelicula = "Interestelar"
genero_pelicula = 5
duracion_pelicula = 169
calificacion_pelicula = 8.7

# Se comparan las preferencias del usuario con los datos de la película
genero_coincide = comparar_genero(genero_escogido, genero_pelicula)
calificacion_coincide = comparar_calificacion(calificacion_pelicula, calificacion_minima)
duracion_coincide = comparar_duracion(duracion_escogida, duracion_pelicula)

# Se decide si la película coincide con las preferencias
pelicula_recomendada = decidir_recomendacion(genero_coincide,duracion_coincide,calificacion_coincide)
if pelicula_recomendada:
    print("\nEncontramos una pelicula que coincide con tus preferencias!")
    mostrar_pelicula(nombre_pelicula, duracion_pelicula, calificacion_pelicula)
else:
    print("\n La unica pelicula que tenemos actualmente en el " \
    "programa no coincide conmpletamente con tus preferencias :(")
    # Resultados comparativos entre la película seleccionada y lo que busca el usuario
    print("\n--- Resultado de las comparaciones ---")
    print("¿Coincide el genero?", genero_coincide)
    print("¿Cumple la duracion seleccionada?", duracion_coincide)
    print("¿Cumple la calificacion minima?", calificacion_coincide)