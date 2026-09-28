sonlar = [2, 5, 2, 8, 5, 9, 2, 8, 10, 5]

def takrorlanmas_sonlar(sonlar):
    natija = []

    for son in sonlar:
        if son not in natija:
            natija.append(son)

    return natija

print(takrorlanmas_sonlar(sonlar))