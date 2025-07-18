
def es_segura(password):

    if len(password) >= 8:
        characters = [x for x in password]
        upper = any(may.isupper() for may in characters)
        digit = any(may.isdigit() for may in characters)
        letter = any(may.isalpha() for may in characters)
        low = any(may.islower() for may in characters)
        simbol = any(33 <= ord(may) <= 47 for may in characters)

    return all([upper, digit, letter, low, simbol])


def main():

    while True:
        s = input('Ingrese password:')
        result = es_segura(s)
        if result:
            print('Fuerte')
            break
        else:
            print('debil')


if __name__ == '__main__':
    main()
