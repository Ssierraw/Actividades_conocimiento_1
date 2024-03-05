#Calculadora de costo de minutos

print ("A dónde deseas llamar?")
print("\n1. Estados Unidos")
print("2. Canadá")
print("3. Europa")
print("4. Resto del mundo")
destino = int(input("Seleccione destino: "))

cantidad = int(input("Ingrese cantidad de minutos gastados: "))

if destino >= 1 and destino <= 4:
    if destino == 1:
        tarifa = 900
    elif destino == 2:
        tarifa = 800
    elif destino == 3:
        tarifa = 950
    else:
        tarifa = 1250

    costo_total = tarifa * cantidad
    descuento = 0
    if cantidad >= 15:
        descuento = costo_total * 0.20

    costo_total = costo_total - descuento
    print(f"El costo de llamada total es de: {costo_total}")
else:
    print("El destino seleccionado es incorrecto")