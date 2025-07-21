
def collatz(n):
    print(f"{n}->", end=' ')
    while n != 1:
        if n % 2 == 0:
            n = n/2
            print(f"{n}->", end=' ')
        else:
            n = 3*n+1
            print(f"{n}->", end=' ')


if __name__ == '__main__':
    collatz(6)
