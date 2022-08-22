from random import randint

def guess(y=10, x = 1):
    isSet = False
    while not(isSet):
        try:
            strzał = int(input("Zgaduj: "))
            assert x <= strzał <= y
        except ValueError:
            print("Zły inpyt! Spróbuj ponownie")
        except AssertionError:
            print(f"Liczba nie w przediale! Wybierz liczbe z przedziału od {x} do {y}")
        else:
            isSet = True
    return strzał

def LoopedGuesser(y=10, x=1):
    random_num=randint(x, y)
    print(f"Zgadnij numer między {x} a {y}!")
    strzał = 0.999
    while strzał!=random_num:
        strzał = guess(y, x)
        if strzał > random_num: print("Nie trafiłeś! Liczba jest mniejsza")
        elif strzał < random_num: print("Nie trafiłeś! Liczba jest wieksza")
    print(f"Brawo! odgadłeś liczbę. To było: {random_num}")

LoopedGuesser(0,0)
print('+'*30)
LoopedGuesser()
print('+'*30)
LoopedGuesser(5)
print('+'*30)
LoopedGuesser(10, 5)
