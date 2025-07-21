def encuesta_satisfaccion(*args, **kwargs):
    respuestas = args
    respuestas_validas = kwargs.get(
        "respuestas_validas", list(set(respuestas)))

    conteo = {}
    total_validas = 0

    for respuesta in respuestas:
        if respuesta in respuestas_validas:
            conteo[respuesta] = conteo.get(respuesta, 0) + 1
            total_validas += 1

    resumen = {}
    for respuesta in respuestas_validas:
        cantidad = conteo.get(respuesta, 0)
        porcentaje = (cantidad / total_validas *
                      100) if total_validas > 0 else 0
        resumen[respuesta] = {
            "cantidad": cantidad,
            "porcentaje": round(porcentaje, 2)
        }

    return resumen


print(encuesta_satisfaccion("bueno", "malo",
      respuestas_validas=["bueno", "malo"]))
