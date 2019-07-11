def ortBul(liste):
    toplam = 0
    for i in liste:
        toplam = toplam + i #toplam += i
    return toplam  / len(liste)

liste = [1,2,3,4,5,6,7,8,9,10]

print(ortBul(liste))
