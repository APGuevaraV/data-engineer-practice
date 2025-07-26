with open('frutas.txt', 'r', encoding='utf8') as frutas:
    frutass = [fruta.strip() for fruta in frutas]
    result = {
        fruta: frutass.count(fruta)
        for fruta in frutass
    }
    print(result)
