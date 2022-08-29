lista_słów = ["kot", "kotek", "koteczek", "pies", "płot", "skok", "ząb", "dąb", "drzewo", "trójkąt", "żółć",
 "strój", "krój", "król", "kraj", "wół", "wóz", "wąż", "mół" "młot", "młotek", "młoteczek", "młynek", "młyneczek",
  "mydło", "mydelniczka", "sól", "solniczka", "kołyska", "kołysanie", "statek", "maszt", "szcotka", "konik", "koń",
   "klacz", "klon", "dąb", "głąb", "wąs", "wąsy", "mysz", "szczur", "wór", "gbór", "małpa", "żółw", "żók", "wąż",
   "pyton", "boa", "baba", "chłop", "pole", "opole", "warszawa", "gdynia", "wrocław", "kijanka", "żaba", "obraz",
   "malarz", "tancerz", "akrobata", "lekarz", "prawnik", "pielęgniarka", "pacha", "rower", "samochód", "auto", "stół",
   "mół", "błoto", "ziemia", "księżyc", "mars", "słońce", "bóg", "niebo", "ogień", "błysk", "światło", "światłość"]

import random
from re import A

def weź_słowo(słowa):
    słowo = random.choice(słowa)
    return słowo


def hangman():
    hasło = weź_słowo(lista_słów).upper()
    litery_hasła = set(hasło)
    litery_użyte = set()
    alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwxyzźżqv".upper()

    życie = ["x" for i in range(11)]
    
    # print("cheat3000:")
    # print(hasło)
    # print()

    print("HASŁO :", wyświetl_hasło(hasło, litery_hasła))
    print("ŻYCIE :", ' '.join(życie))

    while(litery_hasła and życie):
        try:
            print()
            strzał = input("PODAJ ZNAK :").upper()
            
            strzał = strzał[0]
            assert strzał in alfabet

        except AssertionError:
            print("NIEWŁAŚCIWY INPUT")
        except IndexError:
            print("INPUT NIE MOŻE BYĆ PUSTY")

        else:
            
            print("=" * 30)

            if strzał in litery_użyte:
                print("JUŻ UŻYŁEŚ TEGO ZNAKU")

            elif strzał in litery_hasła:
                print("*** TRAFIŁEŚ ***".center(30))
                litery_hasła.remove(strzał)

            else:
                print("*** NIE TRAFIŁEŚ ***".center(30))
                życie.pop()

            litery_użyte.add(strzał)

            print("HASŁO :", wyświetl_hasło(hasło, litery_hasła))
            print("UŻYTE LITERY :", litery_użyte)
            print("ŻYCIE :", ' '.join(życie))

    print()
    print("=" * 30)
    if życie:
        print("*** ZWYCIĘSTWO!!! ***".center(30))
        print("=" * 30)
    else:
        print("*** PRZEGRANA ***".center(30))
        print("=" * 30)
        print("HASŁEM BYŁO SŁOWO :", hasło)


def wyświetl_hasło(hasło, litery_hasła):
    wydruk = ""
    for ch in hasło:
        if ch in litery_hasła:
            wydruk += "- "
        else:
            wydruk += ch+" "
    return wydruk


hangman()