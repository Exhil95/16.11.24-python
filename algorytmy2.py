#Witaj swiecie!
#1
#Xjubk txjfdjf!
#4
#Amxen wamigmi!

s = "Witaj swiecie!"
k = 4

def szyfr_cezara(slowo, klucz):
    try:
        wynik = ""
        slowo = slowo.lower()
    
        for znak in slowo:
            znak_a = ord(znak)

            if znak_a <= ord('z') and znak_a >= ord('a'):
                znak_a += klucz
                if znak_a > ord('z'):
                    znak_a -= 26
            
            wynik = wynik + chr(znak_a)
        return wynik
    except TypeError as e:
        print("TypeError", repr(e))        
        return "TypeError"
    except BaseException as e:
        print(repr(e))
        return "Error"

print("Wiadomość do zaszyfrowania: ", s)
print("Szyfr cezara, klucz 4: ",szyfr_cezara(s,k).capitalize())
print("Szyfr cezara, klucz 13 (ROT13): ",szyfr_cezara(s,13).capitalize())

#Witaj swiecie!
#Drgzq hdrwxrw!

def szyfr_atbasz(slowo):
    wynik = ""
    slowo = slowo.lower()

    for znak in slowo:
        znak_a = ord(znak)
        
        if znak_a <= ord('z') and znak_a >= ord('a'):
            znak_a = ord('z') - (znak_a - ord('a'))
        wynik = wynik + chr(znak_a)

    return wynik

print("Szyfr atbasz: ", szyfr_atbasz(s).capitalize())

def prosty_szyfr_podst(slowo, alfabet):
    wynik = ""
    slowo = slowo.lower()

    for znak in slowo:
        znak_a = ord(znak)
        
        if znak_a <= ord('z') and znak_a >= ord('a'):
            znak_a = znak_a - 97
            wynik = wynik + alfabet[znak_a]
        else:
            wynik = wynik + znak

    return wynik

klucz = "qwertyuiopasdfghjklzmxnbcv"

print("Prosty szyfr podstawieniowy, klucz:",klucz,": ",prosty_szyfr_podst(s,klucz))


#################
slownik = {}
#           klucz   wartość
slownik = {"cat" : "kot",
           "cipher" : "szyfr",
           "tree" : "drzewo",
           "wiek" : 12,
           23 : True,
           True: 56.2,
           86.32 : 122}

print(slownik)
#slownik(slownik[0])
print(slownik["cat"])
print(slownik[23])
print(len(slownik))
print(slownik.keys())

for element in slownik:
    print(element, slownik[element])

print(slownik.items())
for para in slownik.items():
    print(para, para[0], para[1])

for element in slownik.values():
    print(element)

slownik["wiek"] = 30
print("wiek", slownik["wiek"])

slownik["nowy_klucz"] = "nowa wartość"
print(slownik)

del slownik["nowy_klucz"]
print(slownik)

try:
    a = 10
    b = 11
    wynik = 0
    wynik = a + b
    wynik = wynik * 3
    wynik = wynik / 2
    wynik = slownik["nieistniejący klucz"]
except ZeroDivisionError:
    print("Jest błąd! Dzielenie przez 0!")
except TypeError as e:
    print("Błąd typów!", repr(e))
except BaseException as e:
    print("Nieznany błąd!", repr(e))
    
print("Dalsze działanie")
