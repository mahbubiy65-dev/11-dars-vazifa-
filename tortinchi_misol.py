baholar = {
    "Ali": 78,
    "Vali": 45,
    "Hasan": 91,
    "Husan": 56,
    "Sardor": 67
}

def natijalar(baholar):
    for ism, baho in baholar.items():
        if baho >= 60:
            print(ism, "-", baho, "- O'tdi")
        else:
            print(ism, "-", baho, "- Yiqildi")

natijalar(baholar)