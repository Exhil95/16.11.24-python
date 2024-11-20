slowa = input("Podaj słowa do sprawdzenia: (oddzielaj spacją): ").split()

def listy_anagramow(slowa):
    anagramy = {}
    
    for i in slowa: 
        klucz = ''.join(sorted(i))
        if klucz in anagramy:
            anagramy[klucz].append(i)
        else:
            anagramy[klucz] = [i]
    
    return list(anagramy.values())

pogrupowane = listy_anagramow(slowa)


print("Grupy anagramów:")
for j in pogrupowane:
    print(j)