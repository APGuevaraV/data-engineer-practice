import random

number_to_search = random.randint(1, 300)
tries = 0
total_tries = 7
print("Adivina el número mágico, tienes 7 intentos!")
while tries != total_tries:
    search = int(input(f"Intento {tries + 1}:"))
    distance = abs(number_to_search - search)
    if distance == 0:
        print('Lo encontraste')
        break
    elif 1 <= distance <= 10:
        print("Muy cerca")
    elif 11 <= distance <= 20:
        print("Cerca")
    else:
        print('Muy lejos')
    tries += 1
