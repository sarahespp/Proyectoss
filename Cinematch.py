# CineMatch Avance 7
# Matrices

# Matriz que guarda los datos de cada película:
# nombre, género, duración en minutos y calificación.
peliculas = [
    ["Toy Story", "Animación", 81, 8.3],
    ["Spider-Man: Un nuevo universo (2018)", "Animación", 117, 8.4],
    ["El rey león", "Animación", 88, 8.5],
    ["Shrek", "Animación", 90, 7.9],
    ["Cars", "Animación", 117, 7.2],
    ["Cómo entrenar a tu dragón", "Animación", 98, 8.1],

    ["Escuela de rock", "Comedia", 109, 7.2],
    ["Son como niños", "Comedia", 102, 6.0],
    ["Mentiroso, mentiroso", "Comedia", 87, 6.9],
    ["The Truman Show", "Comedia", 103, 8.2],
    ["Viernes de locos", "Comedia", 97, 6.3],

    ["Orgullo y prejuicio", "Romance", 129, 7.8],
    ["Diario de una pasión", "Romance", 123, 7.8],
    ["La La Land", "Romance", 128, 8.0],
    ["Titanic", "Romance", 195, 7.9],
    ["10 cosas que odio de ti", "Romance", 97, 7.3],
    ["Eterno resplandor de una mente sin recuerdos", "Romance", 108, 8.3],

    ["El silencio de los inocentes", "Suspenso", 118, 8.6],
    ["Sexto sentido", "Suspenso", 107, 8.2],
    ["Intriga (Prisoners)", "Suspenso", 153, 8.2],
    ["Parásitos", "Suspenso", 132, 8.5],
    ["La isla siniestra", "Suspenso", 138, 8.2],

    ["Interestelar", "Ciencia ficción", 169, 8.7],
    ["Volver al futuro", "Ciencia ficción", 116, 8.5],
    ["Jurassic Park", "Ciencia ficción", 127, 8.2],
    ["2001: Odisea del espacio", "Ciencia ficción", 149, 8.3],
    ["El origen (Inception)", "Ciencia ficción", 148, 8.8],
    ["La llegada (Arrival)", "Ciencia ficción", 116, 7.9]
]

# Muestra el mensaje de bienvenida al usuario.
def mostrar_bienvenida():
    print("Bienvenido a CineMatch")
    print("Encuentra una película de acuerdo con tus preferencias.")


# Muestra los géneros disponibles y devuelve el seleccionado.
def pedir_genero():
    print("\nSelecciona un género:")
    print("1. Animación")
    print("2. Comedia")
    print("3. Romance")
    print("4. Suspenso")
    print("5. Ciencia ficción")

    genero = int(input("Escribe el número del género que prefieres: "))

    # Convierte el número elegido en el nombre del género.
    if genero == 1:
        return "Animación"
    elif genero == 2:
        return "Comedia"
    elif genero == 3:
        return "Romance"
    elif genero == 4:
        return "Suspenso"
    else:
        return "Ciencia ficción"


# Pide la duración preferida y devuelve la opción seleccionada.
def pedir_duracion():
    print("\nSelecciona una duración:")
    print("1. Corta (menos de 1:30hr)")
    print("2. Media (entre 1:30hr y 2:hr)")
    print("3. Larga (más 2 hr)")

    duracion = int(input("Escribe el número de la duración que prefieres: "))
    return duracion


# Pide la calificación mínima que debe tener la película.
def pedir_calificacion():
    print("\nSelecciona la calificación mínima:")
    print("1. 6.0")
    print("2. 7.0")
    print("3. 8.0")

    calificacion = int(input("Escribe el número de la calificación mínima: "))
    return calificacion


# Convierte la duración en minutos a horas completas.
def calcular_horas(minutos):
    return minutos // 60


# Obtiene los minutos que sobran después de calcular las horas.
def calcular_minutos_restantes(minutos):
    return minutos % 60


# Muestra el nombre, género, duración y calificación de una película.
def mostrar_pelicula(nombre, genero, duracion, calificacion):
    horas = calcular_horas(duracion)
    minutos = calcular_minutos_restantes(duracion)

    print("\nPelícula recomendada:")
    print("Nombre:", nombre)
    print("Género:", genero)
    print("Duración:", horas, "h", minutos, "min")
    print("Calificación:", calificacion)


# Compara el género elegido por el usuario con el de la película.
def comparar_genero(genero_usuario, genero_pelicula):
    return genero_usuario == genero_pelicula


# Verifica si la duración de la película cumple con la opción elegida.
def comparar_duracion(duracion_usuario, duracion_pelicula):
    if duracion_usuario == 1:
        return duracion_pelicula < 90
    elif duracion_usuario == 2:
        return duracion_pelicula >= 90 and duracion_pelicula <= 120
    else:
        return duracion_pelicula > 120


# Verifica si la película alcanza la calificación mínima seleccionada.
def comparar_calificacion(calificacion_usuario, calificacion_pelicula):
    if calificacion_usuario == 1:
        return calificacion_pelicula >= 6.0
    elif calificacion_usuario == 2:
        return calificacion_pelicula >= 7.0
    else:
        return calificacion_pelicula >= 8.0


# Busca películas que coincidan con las preferencias del usuario.
def decidir_recomendacion(genero, duracion, calificacion, peliculas):
    encontro_pelicula = False

    # Recorre la matriz y obtiene los datos de cada película.
    for pelicula in peliculas:
        nombre_actual = pelicula[0]
        genero_actual = pelicula[1]
        duracion_actual = pelicula[2]
        calificacion_actual = pelicula[3]

        # Compara los tres criterios con las preferencias del usuario.
        coincide_genero = comparar_genero(genero, genero_actual)
        coincide_duracion = comparar_duracion(duracion, duracion_actual)
        coincide_calificacion = comparar_calificacion(calificacion, calificacion_actual)

        # Si coinciden los tres criterios, muestra la película.
        if coincide_genero and coincide_duracion and coincide_calificacion:
            mostrar_pelicula(
                nombre_actual,
                genero_actual,
                duracion_actual,
                calificacion_actual
            )
            encontro_pelicula = True

    # Si no hubo coincidencias en los tres criterios, busca películas
    # que coincidan exactamente en dos de ellos.
    if encontro_pelicula == False:
        print("\nNo encontramos una película que coincida con tus 3 preferencias.")
        print("Estas películas coinciden con 2 de tus preferencias:")

        encontro_dos = False

        # Revisa nuevamente cada película y cuenta sus coincidencias.
        for pelicula in peliculas:
            nombre_actual = pelicula[0]
            genero_actual = pelicula[1]
            duracion_actual = pelicula[2]
            calificacion_actual = pelicula[3]

            coincidencias = 0

            if comparar_genero(genero, genero_actual):
                coincidencias += 1

            if comparar_duracion(duracion, duracion_actual):
                coincidencias += 1

            if comparar_calificacion(calificacion, calificacion_actual):
                coincidencias += 1

            # Si coincide exactamente en dos criterios, recomienda la película.
            if coincidencias == 2:
                mostrar_pelicula(
                    nombre_actual,
                    genero_actual,
                    duracion_actual,
                    calificacion_actual
                )
                encontro_dos = True

        # Informa si tampoco se encontraron películas con dos coincidencias.
        if encontro_dos == False:
            print("No encontramos películas que coincidan con tus preferencias.")


# Función principal que organiza la ejecución del programa.
def main():
    mostrar_bienvenida()
    busqueda = "si"

    # Repite la búsqueda mientras el usuario quiera continuar.
    while busqueda == "si":

        # Obtiene las tres preferencias del usuario.
        genero = pedir_genero()
        duracion = pedir_duracion()
        calificacion = pedir_calificacion()

        # Envía las preferencias y la matriz a la función de recomendaciones.
        decidir_recomendacion(
            genero,
            duracion,
            calificacion,
            peliculas
        )
        # Pregunta si el usuario quiere realizar otra búsqueda.
        busqueda = input("\n¿Quieres buscar otra película? (si/no): ")

    print("\n¡Gracias por usar CineMatch!")

# Inicia el programa llamando a la función principal.
main()