def saludar(name, say_hi='Hi!'):
    print(f"{name} {say_hi}")


saludar('Ana')
saludar('María', 'Hola')
saludar('Lurdes', 'Que tal!')


def sumar_todos(*args):
    print(sum(args))


sumar_todos(2, 4, 6, 8, 10)


def perfil_usuario(**datos):
    for x in datos.keys():
        print(f"{x} : {datos[x]}")


perfil_usuario(nombre="Ana", edad=25, ciudad="Lima")


def describir_evento(*args, **kwargs):
    print(list(args))
    print(kwargs)


describir_evento("charla", 2025, "virtual", tema="IA",
                 orador="Ana", duracion="1h")


def operar(operacion, a, b):
    def sumar():
        return a + b

    def restar():
        return a-b

    if operacion == 'suma':
        return sumar()

    else:
        return restar()


print(operar('suma', 5, 145))
print(operar('restar', 5, 145))


def potenciador(exponente):
    def elevar(n):
        return n ** exponente
    return elevar


potencia = potenciador(5)
print(potencia(2))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(2))

# Generador de reportes con formato opcional


def generar_reporte(*datos, encabezado=True):
    if encabezado:
        print('Reporte:')
        for x in datos:
            print(x, end='|')


generar_reporte('Ana', 'Juego', 12, 'Paraguas', encabezado=True)


def validar_enteros(*numeros):
    return [True if numero > 0 else False for numero in numeros]


print()
print(validar_enteros(5, 7, 9, 4, -5, -7, 8, 12, -654, 74, 785, -323))


def crear_usuario(nombre, **opciones):

    usuario = {
        'nombre': nombre,
        'edad': opciones.get('edad', None),
        'email': opciones.get('email', None),
        'activo': opciones.get('activo', False),
    }
    return usuario


print(crear_usuario('Ana'))
print(crear_usuario('Analí', edad=29, email='aaa@aaa.com', activo=False))


def registrar_funcion(nombre_funcion, *args, **kwargs):
    print(nombre_funcion)
    [print(x, end=' ') for x in args]
    print()
    for c, v in kwargs.items():
        print(c, v)


registrar_funcion('Sumar', 'a', 'b', 'c', 'y', 'p', nombre='Lola',
                  edad='29', carrera='Ing')


def crear_multiplicador(factor):
    def multiplica(n):
        return n*factor
    return multiplica


muplity_five = crear_multiplicador(5)
print(muplity_five(6))
multiply_twelve = crear_multiplicador(12)
print(multiply_twelve(9))


def evaluador(valor):
    def es_par():
        return valor % 2 == 0

    def es_positivo():
        return valor > 0

    def es_multiplo_de_3():
        return valor % 3 == 0

    return {
        'par': es_par(),
        'positivo':  es_positivo(),
        'multiplo de 3': es_multiplo_de_3(),
    }


print(evaluador(-135))
print(evaluador(1548))


def buscar_clave(dato_buscado, **kwargs):
    def coincide(clave, valor):
        if valor == dato_buscado or (dato_buscado in valor):
            print(clave)

    for c, v in kwargs.items():
        coincide(c, v)


buscar_clave('15', edad='15', nombre='Ana', peso='65', color='yellow')


def procesar_lista(lista, modo='mayusculas'):
    def mayusculas():
        [print(x.upper()) for x in lista]

    def minusculas():
        [print(x.lower()) for x in lista]

    def capitalizar():
        [print(x.capitalize()) for x in lista]

    if modo == 'mayusculas':
        mayusculas()
    elif modo == 'minusculas':
        minusculas()
    else:
        capitalizar()


procesar_lista(['Ana Guevara', 'Mayra', 'carro', 'proBlema',
               'perro', 'Loro'], modo='mayusculas')


def descuento(precio, tipo="regular"):
    def regular():
        return precio - (precio * 0.1)

    def vip():
        return precio - (precio * 0.2)

    def staff():
        return precio - (precio * 0.3)

    if tipo == 'regular':
        print(f"Total incluido en 10% de descuento : {regular()}")
    elif tipo == 'vip':
        print(f"Total incluido en 20% de descuento : {vip()}")
    else:
        print(f"Total incluido en 30% de descuento : {staff()}")


descuento(200, tipo='regular')
descuento(350, tipo='vip')
descuento(200, tipo='staff')


def verificar_configuracion(*args, **kwargs):
    result = {}
    for x in args:
        if x in result:
            pass
        else:
            if x in kwargs.keys():
                result[x] = True
            else:
                result[x] = False
    return result


rsult = verificar_configuracion('casa', 'edad', 'nombre',
                                'color', color='yellow', nombre='Ana')
print(rsult)
