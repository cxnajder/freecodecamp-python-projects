###################################################################################################
'''Computer Guesser'''

from random import randint

def CompGuess(x, y, tajna, count):
        compguess = randint(x, y)
        print(f"CPU: Wybieram liczbę z zakresu <{x}, {y}> : {compguess}. (Próba nr: {count})")
        if compguess > tajna:
            print("Tajna liczba jest mniejsza")
            CompGuess(x, compguess-1, tajna, count+1)
        elif compguess < tajna:
            print("Tajna liczba jest większa")
            CompGuess(compguess+1, y, tajna, count+1)
        else:
            print(f"Gratulacje odgadłeś liczbę {tajna}")


def SetIntInput(str):
    isSet = False
    x = 0
    while not(isSet):
        try:
            x = int(input(str))
        except ValueError:
            print("Invalid input")
        else:
            isSet = True
    return x


def game():
    isSet = False
    while not(isSet):
        try:
            x=SetIntInput("dolna wartość zakresu:")
            y=SetIntInput("górna wartość zakresu:")
            tajnaliczba=SetIntInput("Tajna liczba:")
            assert x <= tajnaliczba <= y
        except AssertionError:
            print("Próba oszukania komputera lub przejaw głupoty.\nProszę wprowadzić poprawne dane.")
        else:
            isSet = True
    CompGuess(x, y, tajnaliczba, 1)

game()
