nota = input("Ingresa tu nota del 1 al 5: ")
nota = float(nota)

if 0 <= nota <=5:

    if 4 <= nota <= 5:
        print("Tu nota es excelente.")
    elif 3 <= nota <= 4:
        print("Tu nota es Buena.")
    elif 0 <= nota <= 2.99:
        print("Tu nota es Deficiente.")
else:
    print("Numero inválido, por favor ingresa un número del 0 al 5")

#Notificacion en caso de que el estudiante tenga una nota excelente

if 4 <= nota <= 5:
    print("¡Felicitaciones! Tienes un 20% de descuento en tu matrícula")