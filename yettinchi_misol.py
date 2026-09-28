sirli_son = 37

def son_topish(sirli_son):
    while True:
        son = int(input("Son kiriting: "))

        if son > sirli_son:
            print("Kichikroq son kiriting")
        elif son < sirli_son:
            print("Kattaroq son kiriting")
        else:
            print("Tabriklayman!")
            break

son_topish(sirli_son)