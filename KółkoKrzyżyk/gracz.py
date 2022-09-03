class Gracz:
    __licznik = 0
    def __init__(self, znak = 'o'):
        self.__znak = znak
        Gracz.__licznik += 1
        self.__nazwa = f"Gracz {self.__licznik}"

    @classmethod
    def NowaGra(cls):
        cls.__licznik = 0

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def znak(self):
        return self.__znak

    def Wybor(self, wybrana_liczba):
        poziom = (wybrana_liczba - 1) // 3
        pion = (wybrana_liczba - 1) % 3
        return (self.__znak, poziom, pion)

    def WyborPodpowiedz(self, lista_wolnych_pol = [i for i in range(1, 10)], zajete_przez_o = []):
        print("Numery pól do wyboru:")
        print("+---" * 3 + "+") # da to samo co: print("+---+---+---+")
        for i in range(9):
            if i + 1 in lista_wolnych_pol:
                print(f"| {i + 1} ", end="")
            elif not zajete_przez_o:
                print(f"|   ", end="")
            else:
                if i + 1 in zajete_przez_o:
                    print(f"| o ", end="")
                else:
                    print(f"| x ", end="")
            if (i+1) % 3 == 0:
                print("|")
                print("+---" * 3 + "+") # da to samo co: print("+---+---+---+") 
        # +---+---+---+
        # | 1 | 2 | 3 |
        # +---+---+---+
        # | 4 | 5 | 6 |
        # +---+---+---+
        # | 7 | 8 | 9 |
        # +---+---+---+

class GraczCzlowiek (Gracz):
    def __init__(self, znak):
        super().__init__(znak)
            
    def Wybor(self, lista_wolnych_pol = [i for i in range(1, 10)]):
        while True:
            try:
                wybrana_liczba = int(input("Wybierz pole (1-9): "))
                assert 1 <= wybrana_liczba <= 9, "Niewłaściwy zakres"
                assert wybrana_liczba in lista_wolnych_pol
                return super().Wybor(wybrana_liczba)
            except ValueError:
                print("Niwłaściwy input")
            except AssertionError:
                print("Wybór z poza dostępnego zakresu")
                raise
    
import random

class GraczKomp (Gracz):
    def __init__(self, znak='o'):
        super().__init__(znak)

    def Wybor(self, lista_wolnych_pol = [i for i in range(1, 10)]):
        wybrana_liczba = random.choice(lista_wolnych_pol)
        print(f"Komputer wybrał pole {wybrana_liczba}")
        return super().Wybor(wybrana_liczba)

if __name__ == "__main__":
    gracz1 = GraczCzlowiek('x')
    print(gracz1._Gracz__licznik)
    gracz1.WyborPodpowiedz()
    print(gracz1.Wybor())

    gracz2 = GraczKomp('o')
    print(gracz2._Gracz__licznik)
    print(gracz2.Wybor())
    print(Gracz._Gracz__licznik)
    print(Gracz.NowaGra())
    print(Gracz._Gracz__licznik)