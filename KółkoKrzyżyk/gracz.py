class Gracz:
    def __init__(self, znak = 'o'):
        self.znak = znak

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
                poziom = (wybrana_liczba - 1) // 3
                pion = (wybrana_liczba - 1) % 3
                return (self.znak, poziom, pion)
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
        poziom = (wybrana_liczba - 1) // 3
        pion = (wybrana_liczba - 1) % 3
        return (self.znak, poziom, pion)

if __name__ == "__main__":
    gracz1 = GraczCzlowiek('x')
    gracz1.WyborPodpowiedz()
    print(gracz1.Wybor())

    gracz2 = GraczKomp('o')
    print(gracz2.Wybor())