date_to_format = int(input('Ingresa número de segundos:'))
horas, minutos = divmod(date_to_format, 3600)
minutos_totales, segundos_totales = divmod(minutos, 60)

print(f"{horas} horas, {minutos_totales} minutos,{segundos_totales} segundos")
