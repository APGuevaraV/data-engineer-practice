promedios = {
    "Ana": 18.2,
    "Luis": 15.5,
    "Pedro": 13.7,
    "María": 19.1,
    "Javier": 14.8,
    "Carmen": 17.3,
    "Diego": 12.9,
    "Lucía": 16.4,
    "Andrés": 11.5,
    "Sofía": 18.9,
    "José": 13.0,
    "Valeria": 19.5,
    "Marco": 15.2,
    "Elena": 17.8,
    "Raúl": 10.7,
    "Paula": 14.1,
    "Tomás": 16.6,
    "Daniela": 12.3,
    "Fernando": 13.9,
    "Gabriela": 18.0
}


def ranking_students(promedios):
    print(promedios.get('Ana'))
    claves = sorted(promedios, key=promedios.get, reverse=True)
    print("PUESTO**********Nombre******PROMEDIO")
    for i, c in enumerate(claves):
        print(f"{i+1} -      {c.upper()}      - {promedios[c]}")


ranking_students(promedios)
