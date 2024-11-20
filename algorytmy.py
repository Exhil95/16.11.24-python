cyfry = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 0]
liczba = 9

index = 0
ostatni = len(cyfry) - 1

while index <= ostatni:
    srodek = (index + ostatni) // 2
    print(index)
    if cyfry[srodek] == liczba:
        print("Liczba jest w tablicy")
        break
    if cyfry[srodek] > liczba:
        ostatni = srodek - 1
    else:
        index = srodek + 1
        