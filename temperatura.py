limite_temp = 85.0

while True:
    temp_actual = float(input("Ingresa la temperatura del sensor: "))

    if temp_actual > limite_temp:
        print("ALERTA: Temperatura superior al límite. Peligro de sobrecalentamiento.")
    else:
        print("Temperatura estable.")
        break