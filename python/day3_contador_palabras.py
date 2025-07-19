from collections import Counter

parrafo = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam 
            sit """


def count_words(text) -> int:
    print(f"Cantidad de palabras:{len(text.split())}")


def count_letters(text):
    c = Counter(text)
    print(dict(c))


if __name__ == '__main__':
    count_words(parrafo)
    count_letters(parrafo.lower().replace(
        '\n', '').replace('.', '').replace(',', '').replace(' ', ''))
