slowo1 = str(input("Podaj słowo pierwsze: "))
slowo2 = str(input("podaj słowo drugie: "))

def anagramy(slowo1, slowo2):
     if sorted(slowo1) == sorted(slowo2):
          print(f"{slowo1} i {slowo2} są anagramami")
     else:
          print(f"{slowo1} i {slowo2} nie są anagramami")

anagramy(slowo1, slowo2)