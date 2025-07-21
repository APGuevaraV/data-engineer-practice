import random


def validate(capacidad, nuevo):
    return capacidad >= nuevo


def main():
    packs = []
    capacidad = 100
    while capacidad > 0:

        new_package = random.randint(1, 50)
        print(f"Siguiente peso a llenar:{new_package}")
        if (validate(capacidad, new_package)):
            packs.append(new_package)
            capacidad -= new_package
            print(f"{new_package} descontado : capacidad de caja {capacidad}")

        else:
            print("Demadiado grande, excede capacidad")
            break

        input()
    print(" ".join(map(str, packs)))


if __name__ == '__main__':
    main()
