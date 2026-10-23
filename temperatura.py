limite_temp = 85.0
temp_actual = 90.0 # Simulando lectura de sensor

if temp_actual <= limite_temp:
    print("ALERTA: Temperatura superior al límite. Peligro de sobrecalentamiento.")
else:
    print("Temperatura estable.")