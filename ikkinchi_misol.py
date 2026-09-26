sonlar = []

n = int(input("nechta son kiritasiz: "))

for i in range(n):
    son = int(input("son kiriting: "))
    sonlar.append(son)

def min_max(sonlar):
    katta = sonlar[0]
    kichik = sonlar[0]

    for son in sonlar:
        if son > katta:
            katta = son
        if son < kichik:
            kichik = son

    print(katta)
    print(kichik)

min_max(sonlar)