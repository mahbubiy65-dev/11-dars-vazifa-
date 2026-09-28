kontaktlar = {
    "Ali": "901234567",
    "Vali": "911112233"
}

def kontakt_qidir(kontaktlar, ism):
    if ism in kontaktlar:
        print(kontaktlar[ism])
    else:
        print("Bunday kontakt topilmadi")

ism = input("Ism kiriting: ")

kontakt_qidir(kontaktlar, ism)