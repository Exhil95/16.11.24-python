s = "Gesi lataja kluczem!"
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
    
# wynik = txeom pexene opygdiq!
    
def deszyfr_cezara(slowo, klucz):
    try:
        return "".join(
            chr((ord(znak) - klucz - 97) % 26 + 97) if 'a' <= znak <= 'z' else znak
            for znak in slowo.lower()
        )
    except TypeError as e:
        print("Błąd typu:", repr(e))
        return "Błąd typu"
    except BaseException as e:
        print("Nieoczekiwany błąd:", repr(e))
        return "Nieoczekiwany błąd"

def test_cezara():
    try:
        global s
        global k 
    
        # test na zaszyfrowanie
        zaszyfrowane = szyfr_cezara(s, k)
        print("Szyfr Cezara - zaszyfrowane:", zaszyfrowane)

        #  test na deszyfrowanie
        odszyfrowane = deszyfr_cezara(zaszyfrowane, k)
        print("Szyfr Cezara - odszyfrowane:", odszyfrowane)

        # Sprawdzenie wyniku
        assert odszyfrowane == s.lower(), "Test szyfru Cezara nie powiódł się"
        print("Test szyfru Cezara: OK")
    except AssertionError as e:
        print("Test szyfru Cezara nie powiódł się:", e)
    except Exception as e:
        print("Nieoczekiwany błąd w szyfrze Cezara:", repr(e))

test_cezara()


def szyfr_atbasz(slowo):
    wynik = ""
    slowo = slowo.lower()

    for znak in slowo:
        znak_a = ord(znak)
        
        if znak_a <= ord('z') and znak_a >= ord('a'):
            znak_a = ord('z') - (znak_a - ord('a'))
        wynik = wynik + chr(znak_a)

    return wynik

#wynik Kgzpr ozgzqz pofxavn!


def deszyfr_atbasz(slowo):
    try:
        wynik = ""
        slowo = slowo.lower()

        for znak in slowo:
            znak_a = ord(znak)
            
            if znak_a <= ord('z') and znak_a >= ord('a'):
                znak_a = ord('z') - (znak_a - ord('a'))
            wynik = wynik + chr(znak_a)
        
        return wynik
    except TypeError as e:
        print("Błąd typu:", repr(e))
        return "Błąd typu"
    except BaseException as e:
        print("Nieoczekiwany błąd:", repr(e))
        return "Nieoczekiwany błąd"


def test_atbasz():
    try:
        global s

        # Szyfrowanie
        zaszyfrowane = szyfr_atbasz(s)
        print("Szyfr Atbasz - zaszyfrowane:", zaszyfrowane)

        # Deszyfrowanie
        odszyfrowane = deszyfr_atbasz(zaszyfrowane)
        print("Szyfr Atbasz - odszyfrowane:", odszyfrowane)

        # Sprawdzenie 
        assert odszyfrowane == s.lower(), "Test szyfru Atbasz nie powiódł się"
        print("Test szyfru Atbasz: OK")
    except AssertionError as e:
        print("Test szyfru Atbasz nie powiódł się:", e)
    except Exception as e:
        print("Nieoczekiwany błąd w szyfrze Atbasz:", repr(e))
        
test_atbasz()


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
#wynik utlo sqzqpq asmevtd!


def deszyfr_podst(slowo, alfabet):
    try:
        odwrotny_klucz = {alfabet[i]: chr(i + 97) for i in range(len(alfabet))}
        wynik = ""
        slowo = slowo.lower()

        for znak in slowo:
            if znak in odwrotny_klucz:
                wynik += odwrotny_klucz[znak]
            else:
                wynik += znak

        return wynik
    except TypeError as e:
        print("Błąd typu:", repr(e))
        return "Błąd typu"
    except BaseException as e:
        print("Nieoczekiwany błąd:", repr(e))
        return "Nieoczekiwany błąd"


def test_podst():
    try:
        global s  
        global klucz 

        # Szyfrowanie
        zaszyfrowane = prosty_szyfr_podst(s, klucz)
        print("Szyfr podstawieniowy - zaszyfrowane:", zaszyfrowane)

        # Deszyfrowanie
        odszyfrowane = deszyfr_podst(zaszyfrowane, klucz)
        print("Szyfr podstawieniowy - odszyfrowane:", odszyfrowane)

        # Sprawdzenie 
        assert odszyfrowane == s.lower(), "Test szyfru podstawieniowego nie powiódł się"
        print("Test szyfru podstawieniowego: OK")
    except AssertionError as e:
        print("Test szyfru podstawieniowego nie powiódł się:", e)
    except Exception as e:
        print("Nieoczekiwany błąd w szyfrze podstawieniowym:", repr(e))
test_podst()
