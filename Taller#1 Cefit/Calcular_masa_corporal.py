#Calculadora de masa corporal

print ("Calculemos tu masa corporal")
peso = float(input("Ingrese su peso en Kilos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura**2)

print(f"Tu índice de masa corporal es de {imc:.2f}")

if imc < 18.5:
    print (f"Tu masa corporal es baja")
elif 18.5 <= imc < 24.9:
    print(f"Tu masa corporal es Normal")
elif 25 <= imc < 29.9:
    print(f"Tienes sobrepeso")
else:
    print(f"Tienes obesidad")