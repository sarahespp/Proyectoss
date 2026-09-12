# CineMatch Avance 3
# Uso de funciones


def mostrar_bienvenida():
    print("Bienvenido a CineMatch!")
    print("Encuentra una pelicula de acuerdo con tus preferencias.")


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


def pedir_duracion():
    print("\nDuracion:")
    print("1. Corta (menos de 90 minutos)")
    print("2. Media (de 90 a 120 minutos)")
    print("3. Larga (mas de 120 minutos)")

    duracion_escogida = int(input("Selecciona una duracion (1 al 3): "))
    return duracion_escogida


def pedir_calificacion():
    calificacion_minima = float(input("Indica la calificacion minima que buscas (0 a 10): "))
    return calificacion_minima

def calcular_horas(duracion_pelicula):
    horas = duracion_pelicula // 60
    return horas

def calcular_minutos_restantes(duracion_pelicula):
    minutos = duracion_pelicula % 60
    return minutos

def mostrar_pelicula(nombre_pelicula, duracion_pelicula, calificacion_pelicula):
    horas = calcular_horas(duracion_pelicula)
    minutos = calcular_minutos_restantes(duracion_pelicula)

    print("\n--- Pelicula encontrada ---")
    print("Nombre:", nombre_pelicula)
    print("Duracion:", horas, "horas y", minutos, "minutos")
    print("Calificacion:", calificacion_pelicula)


def comparar_genero(genero_escogido, genero_pelicula):
    return genero_escogido == genero_pelicula

def comparar_calificacion(calificacion_pelicula, calificacion_minima):
    return calificacion_pelicula >= calificacion_minima

def comparar_duracion(duracion_escogida, duracion_pelicula):
    if duracion_escogida == 1:
        return duracion_pelicula < 90
    elif duracion_escogida == 2:
        return 90 <= duracion_pelicula <= 120
    elif duracion_escogida == 3:
        return duracion_pelicula > 120
    else:
        return False

# Programa principal
mostrar_bienvenida()

genero_escogido = pedir_genero()
duracion_escogida = pedir_duracion()
calificacion_minima = pedir_calificacion()

# Datos de una película de ejemplo
nombre_pelicula = "Interestelar"
genero_pelicula = 5
duracion_pelicula = 169
calificacion_pelicula = 8.7

genero_coincide = comparar_genero(genero_escogido, genero_pelicula)
calificacion_coincide = comparar_calificacion(calificacion_pelicula, calificacion_minima)
duracion_coincide = comparar_duracion(duracion_escogida, duracion_pelicula)
mostrar_pelicula(nombre_pelicula, duracion_pelicula, calificacion_pelicula)

print("\n--- Resultado de las comparaciones ---")
print("¿Coincide el genero?", genero_coincide)
print("¿Cumple la duracion seleccionada?", duracion_coincide)
print("¿Cumple la calificacion minima?", calificacion_coincide)