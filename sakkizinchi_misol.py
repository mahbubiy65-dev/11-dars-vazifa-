mahsulotlar = {
    "non": 4000,
    "sut": 10000,
    "shakar": 14000,
    "guruch": 16000,
    "yog'": 18000
}

def savat_hisobla(mahsulotlar):
    savat = []

    while True:
        mahsulot = input("Mahsulot kiriting: ")

        if mahsulot == "stop":
            break

        if mahsulot in mahsulotlar:
            savat.append(mahsulot)
        else:
            print("Bunday mahsulot yo'q")

    jami = 0

    for mahsulot in savat:
        jami += mahsulotlar[mahsulot]

    print("Umumiy narx:", jami)

savat_hisobla(mahsulotlar)