from collections import defaultdict
alumnos = {
    "Ana": 18,
    "Luis": 20,
    "María": 19,
    "Jorge": 20,
    "Lucía": 18
}
# invertir diccionario
edades = defaultdict(list)
for nombre, edad in alumnos.items():
    edades[edad].append(nombre)


print(edades)


def max_eight(password):
    if len(password) >= 8:
        return True
    else:
        return False


def contain_upper(password):
    for letter in password:
        if 65 >= ord(letter) <= 90:
            return True
        else:
            return False


def contain_lower(password):
    for letter in password:
        if 97 >= ord(letter) <= 122:
            return True
        else:
            return False


def password_validation(password):

    eightcharacters = max_eight(password)
    contain_uppers = contain_upper(password)
    contain_lowers = contain_lower(password)

    print('Contraseña Válida:', eightcharacters &
          contain_uppers & contain_lowers)


password = 'Anapaula'
password_validation(password)


# contar ocurrencias
texto = "Python es genial, y Python es poderoso. Me encanta Python!"
formatted = texto.replace('.', '').replace(',', '').replace('!', '').lower()

palabras = set(formatted.split())

result = [(palabra, formatted.count(palabra))
          for palabra in palabras if len(palabra) > 1]

print(result)
