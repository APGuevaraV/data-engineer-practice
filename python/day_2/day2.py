import random


def clasify(notes: list):
    for x in notes:
        if x < 10:
            print(f"{x} - Desaprobado")
        elif x < 18:
            print(f"{x} - Aprobado")
        else:
            print(f"{x} - Excelente")


print("Final Notes:")
notes = [random.randint(0, 20) for x in range(10)]
clasify(notes=notes)


def serie_fibonacci(n):
    a, b = 0, 1
    contador = 0
    serie = []

    while contador < n:
        serie.append(a)
        a, b = b, a + b
        contador += 1

    return serie


print(f"Serie :{serie_fibonacci(25)}")


def high_value(diccionario: dict):
    mayor = max(diccionario, key=diccionario.get)
    return f"{mayor} - {diccionario[mayor]}"


diccionario = {
    'nota1': 17,
    'nota2': 11,
    'nota3': 4,
    'nota4': 9,
    'nota5': 13,
    'nota6': 10,
    'nota7': 15,
    'nota8': 19,
}

print(high_value(diccionario))


def existe(students, clave):
    return clave in students


def add_student(students):
    name = input('Nombre de estudiante:')
    if existe(students, name.lower()):
        print('Ya se encuentra en la lista')
    else:
        students[name.lower()] = {'edad': 0, 'notas': []}


def add_notes(students):
    name = input('Nombre de estudiante:').lower()
    if existe(students, name):
        notas = [int(input('Ingrese nota:')) for x in range(4)]
        students[name]['notas'] += notas
    else:
        print('No existe el registro')
    print(students)


def average(students):
    for key in students.keys():
        notas = students[key]['notas']
        promedio = sum(notas)/len(notas)
        print(f"{key.upper()} - Promedio:{promedio}")


def show_notes(students):
    for key in students.keys():
        notas = students[key]['notas']
        print(f"{key.upper()} - ", end='')
        [print(x, end=' ') for x in notas]
        print()


def main():
    students = dict()

    while True:
        print('************************************************')
        print('Bienvenido al sistema de gestión de estudiantes')
        print('************************************************')
        print('1.Agregar a alumnos')
        print('2.Agregar notas')
        print('3.Calcular promedios')
        print('4.Mostrar lista de alumnos y notas')
        print('5.Salir')
        opcion = int(input('Elija una opción:'))
        if opcion == 1:
            add_student(students)
        elif opcion == 2:
            add_notes(students)

        elif opcion == 3:
            average(students)
        elif opcion == 4:
            show_notes(students)

        if opcion == 5:
            print("Hasta luego")
            break


main()
