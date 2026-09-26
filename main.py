sonlar = [12, 7, 5, 18, 21, 30, 44, 9]

def juft(sonlar):
    res = []
    for i in sonlar:
        if i % 2 == 0:
            res.append(i)
    return res

print(juft(sonlar))