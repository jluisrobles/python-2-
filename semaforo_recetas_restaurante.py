#Reto 1

#Utiliza una secuencia if/else para decidir si un peatón debe cruzar un paso de cebra o no.
print("---------RETO 1---------")
semaforo = str (input("Color de semaforo: "))

if semaforo == "verde":
    print("Puedes cruzar la calle.")
else :
    print("¡Cuidado! No puedes cruzar la calle")

#Reto 2

"""Piensa en una aplicación que proponga recetas de cocina dependiendo del ingrediente
principal.

Utiliza los condicionales para proponer una receta según el ingrediente principal.

Hacerlo para 10 ingredientes principales diferentes.

Por defecto si no coincide el ingrediente con los que se propone, mostrar “Imposible
proponer receta” por consola.

Utiliza los bloques try-except para manejar las posibles excepciones que se produzcan"""

print("---------RETO 2---------")
try:
    ingrediente = str (input("¿Que ingrediente te gustaria para la receta?, en minúsculas: "))

    if ingrediente == "tomate":
        print ("PAN CON TOMATE : podrias untar el tomate en un pan y sazonar con sal y aceita de oliva")
    elif ingrediente == "ajo":
        print("SALSA DE AJO: tritura el ajo con sal, pimienta y aceite a gsuto")
    elif ingrediente == "cebolla":
        print("ENSALADA: Con la cebolla um par de tomates y un pepimo ")
    elif ingrediente == "pepino":
        print("PEPINOS ENCURTIDOS: corta los pepinos en rodajas y dejarlos marinar una semanas")
    elif ingrediente == "aceite":
        print("PARA ALIÑAR: Con un poco de vinagre de modena y sal, perfecto para ensaladas")
    elif ingrediente == "patata":
        print("PAPAS ARRUGADAS: dejar hervir con mucha sal y servir con salsa a gusto")
    elif ingrediente == "pollo":
        print("SOPA DE POLLO: EN abundante agua y con mucha verdura, dejar hervir con sal a gusto")
    elif ingrediente == "huevo":
        print("TORTILLA: con la ayuda de un tedor baitr el huevo con sal y peregil para despues freir en la sarten")
    elif ingrediente == "queso":
        print("QUESO FRITO: lonchas gordas de queso, vuelta y vuelta en la sarten ")
    elif ingrediente == "pulpo":
        print("PULPO A LA GALLEGA: Cortar el pulpo en rodajas y sellar en la sarten, acompañar de patata en rodajas")
    else:
        print("Para este ingrediente no tenemos recetas, pero pronto las tendremos.")
except Exception as e:
        print("Ha ocurrido un error:", e)
finally:
    print("Te esperamos para próximas recetas")

#Reto 3

"""Piensa un escenario en el que se quiere decidir un restaurante para una celebración.
Los organizadores quieren que cumpla uno de los siguientes puntos:

• Que haya 3 platos en el menú, que incluya DJ y dos horas de barra libre.
• Que haya cóctel de bienvenida, menú con dos platos y una hora de barra libre.

Utilizar los bloques try-except-finally para las posibles excepciones que se produzcan"""

print("---------RETO 3---------")
try:
    opcion = int(input("¿Qué requisitos buscas en el restaurante?\n1. 3 platos, DJ y 2 horas de barra libre.\n2. Cóctel de bienvenida, 2 platos y 1 hora de barra libre.\nSelecciona una opción (1-2): "))
    if opcion == 1:
        if True: print("Restaurante cumple requisitos opción 1")
    elif opcion == 2:
        if True: print("Restaurante cumple requisitos opción 2")
    else:
        print("Opción inválida")
except ValueError:
    print("Solo puedes ingresar números 1 - 2")
finally:
    print("¡Gracias por utilizar el programa!")
