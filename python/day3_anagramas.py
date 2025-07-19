def anagrama(first_word, second_word):
    first_word.lower()
    second_word.lower()
    a = sorted(first_word, reverse=True)
    if (''.join(a) == second_word) or (first_word == second_word):
        print("Son anagramas")
    else:
        print("No son anagramas")


if __name__ == '__main__':
    a = input("Primera palabra:")
    b = input("Segunda palabra:")
    anagrama(a, b)
