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
