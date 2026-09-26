mahsulotlar = {
    "non": 4000,
    "sut": 10000,
    "shakar": 14000,
    "yog'": 18000,
    "guruch": 16000
}

def qimmat_mahsulotlar(mahsulotlar):
    for mahsulot, narx in mahsulotlar.items():
        if narx > 15000:
            print(mahsulot, ":", narx)

qimmat_mahsulotlar(mahsulotlar)