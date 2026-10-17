# CineMatch Avance 6
# Listas (arreglos)

# Listas de películas
nombre_pelicula = ["Shrek", "Cars", "Cómo entrenar a tu dragón",
                   "Escuela de Rock", "Son como niños",
                   "Mentiroso mentiroso", "Titanic",
                   "Orgullo y prejuicio", "10 cosas que odio de ti",
                   "Sexto sentido", "Intriga", "Parasite",
                   "Interestelar", "Jurassic Park", "Volver al futuro"]

genero_pelicula = ["Animación", "Animación", "Animación",
                   "Comedia", "Comedia", "Comedia",
                   "Romance", "Romance", "Romance",
                   "Suspenso", "Suspenso", "Suspenso",
                   "Ciencia ficción", "Ciencia ficción",
                   "Ciencia ficción"]

duracion_pelicula = [90, 116, 98, 109, 102, 86, 194, 129, 97, 107, 153, 132, 169, 127, 116]
calificacion_pelicula = [7.9, 7.3, 8.1, 7.2, 6.0, 6.9, 8.0, 7.8, 7.3, 8.2, 8.2, 8.5, 8.7, 8.2, 8.5]

# Función que muestra el mensaje de bienvenida al usuario
def mostrar_bienvenida():
    print("Bienvenido a CineMatch!")
    print("Encuentra una pelicula de acuerdo con tus preferencias.")

# Función que muestra las opciones de género
def pedir_genero():
    print("\nGeneros:")
    print("1. Animación")
    print("2. Comedia")
    print("3. Romance")
    print("4. Suspenso")
    print("5. Ciencia ficcion")

    genero_escogido = int(input("Selecciona un genero (1 al 5): "))
    return genero_escogido

# Función que muestra las opciones de duración
def pedir_duracion():
    print("\nDuracion:")
    print("1. Corta (menos de 90 minutos)")
    print("2. Media (de 90 a 120 minutos)")
    print("3. Larga (mas de 120 minutos)")

    duracion_escogida = int(input("Selecciona una duracion (1 al 3): "))
    return duracion_escogida

# Función que pide la calificación mínima
def pedir_calificacion():
    calificacion_minima = float(input("Indica la calificacion minima que buscas (0 a 10): "))
    return calificacion_minima

# Función que convierte la duración de una película a horas
def calcular_horas(duracion):
    horas = duracion // 60
    return horas

# Función que calcula los minutos restantes
def calcular_minutos_restantes(duracion):
    minutos = duracion % 60
    return minutos

# Función que muestra los datos de una película
def mostrar_pelicula(nombre, duracion, calificacion):
    horas = calcular_horas(duracion)
    minutos = calcular_minutos_restantes(duracion)

    print("\n--- Pelicula encontrada ---")
    print("Nombre:", nombre)
    print(f"Duracion: {horas} horas y {minutos} minutos")
    print("Calificacion:", calificacion)

# Función que compara el género
def comparar_genero(genero_escogido, genero):
    if genero_escogido == 1:
        return genero == "Animación"
    elif genero_escogido == 2:
        return genero == "Comedia"
    elif genero_escogido == 3:
        return genero == "Romance"
    elif genero_escogido == 4:
        return genero == "Suspenso"
    elif genero_escogido == 5:
        return genero == "Ciencia ficción"
    else:
        return False

# Función que compara la calificación
def comparar_calificacion(calificacion, calificacion_minima):
    return calificacion >= calificacion_minima

# Función que compara la duración
def comparar_duracion(duracion_escogida, duracion):
    if duracion_escogida == 1:
        return duracion < 90
    elif duracion_escogida == 2:
        return 90 <= duracion <= 120
    elif duracion_escogida == 3:
        return duracion > 120
    else:
        return False
    
# Función que decide si la película coincide con las preferencias
def decidir_recomendacion(genero_coincide, duracion_coincide, calificacion_coincide):
    if genero_coincide and duracion_coincide and calificacion_coincide:
        return True
    else:
        return False

# Función principal del programa
def main():
    mostrar_bienvenida()
    otra_busqueda = "si"
    while otra_busqueda == "si":
        # Se piden las preferencias del usuario
        genero_escogido = pedir_genero()
        duracion_escogida = pedir_duracion()
        calificacion_minima = pedir_calificacion()

        # Variables para saber si se encontraron películas
        pelicula_encontrada = False
        alternativa_encontrada = False

        # Primera busqueda: las 3 preferencias
        for i in range(len(nombre_pelicula)):
            # Obtiene los datos de la película que ocupa la posición actual en las listas
            nombre_actual = nombre_pelicula[i]
            genero_actual = genero_pelicula[i]
            duracion_actual = duracion_pelicula[i]
            calificacion_actual = calificacion_pelicula[i]

            # Compara el género, la duración y la calificación de la película con 
            # las preferencias del usuario.

            genero_coincide = comparar_genero(genero_escogido, genero_actual)
            duracion_coincide = comparar_duracion(duracion_escogida, duracion_actual)
            calificacion_coincide = comparar_calificacion(calificacion_actual, calificacion_minima)

            # Comprueba si las tres preferencias coinciden para determinar si se recomienda la película.
            pelicula_recomendada = decidir_recomendacion(genero_coincide,duracion_coincide,
                                                         calificacion_coincide)
            
            # Si la película cumple las tres preferencias, muestra sus datos y registra que se encontró una.
            if pelicula_recomendada:
                if not pelicula_encontrada:
                    print("\nEncontramos peliculas que coinciden con todas tus preferencias!")
                mostrar_pelicula(nombre_actual,duracion_actual,calificacion_actual)
                pelicula_encontrada = True
                
        # Segunda búsqueda: si no hubo coincidencias con las tres preferencias,
        # busca películas que cumplan exactamente dos de las tres.
        if not pelicula_encontrada:
            print("\nNo encontramos peliculas que coincidan con todas tus preferencias.")
            print("Pero encontramos estas alternativas con 2 coincidencias:")

            # Recorre nuevamente todas las películas para contar cuántas preferencias cumple cada una.
            for i in range(len(nombre_pelicula)):
                genero_coincide = comparar_genero(genero_escogido, genero_pelicula[i])
                duracion_coincide = comparar_duracion(duracion_escogida, duracion_pelicula[i])
                calificacion_coincide = comparar_calificacion(calificacion_pelicula[i], calificacion_minima)
                
                # Inicializa el contador de coincidencias en cero para la película actual.
                coincidencias = 0

                if genero_coincide:
                    coincidencias = coincidencias + 1

                if duracion_coincide:
                    coincidencias = coincidencias + 1

                if calificacion_coincide:
                    coincidencias = coincidencias + 1
                
                # Si la película cumple exactamente dos preferencias, muestra sus datos
                # y registra que se encontró al menos una alternativa.

                if coincidencias == 2:
                    mostrar_pelicula(nombre_pelicula[i], duracion_pelicula[i],calificacion_pelicula[i])
                    alternativa_encontrada = True
            
            # Si ninguna película cumplió exactamente dos preferencias, muestra un mensaje al usuario.
            if not alternativa_encontrada:
                print("No encontramos peliculas con 2 coincidencias.")
                
        # Se pregunta si el usuario desea realizar otra búsqueda
        otra_busqueda = input("\nQuieres realizar otra busqueda? (si o no): ")

    print("\nGracias por usar CineMatch!")

# Llama a la función principal para iniciar el programa.
main()