# simulacion cajero
import os

saldo = 1000


def hay_saldo_suficiente(saldo, monto):
    return saldo >= monto and saldo > 0


def retirar(saldo, monto):

    if hay_saldo_suficiente(saldo, monto):
        saldo = saldo - monto
        print(f"{monto} soles retirados con éxito")
    else:
        print('No hay saldo suficiente')
    return saldo


def depositar(saldo, monto):
    if monto > 0:
        saldo = saldo + monto
        print(f"{monto} soles depositados con éxito")
    else:
        print('Monto incorrecto, solo montos positivos')
    return saldo


def show_menu():
    os.system('cls')
    print('**********************************')
    print('Gestión de cajero')
    print('**********************************')
    print('1.Retirar dinero')
    print('2.Depositar')
    print('3.Ver saldo')
    print('4.Salir')
    opcion = int(input('Ingresa una opción:'))
    os.system('cls')
    return opcion


def main():

    saldo = 1000
    while True:

        opcion = show_menu()
        if opcion == 1:
            monto = int(input('Monto a retirar:'))
            saldo = retirar(saldo, monto)

        elif opcion == 2:
            monto = int(input('Monto a depositar:'))
            saldo = depositar(saldo, monto)

        elif opcion == 3:
            print(f"Tu saldo actualmente es de :{saldo}")

        else:
            break

        input()


if __name__ == '__main__':
    main()
