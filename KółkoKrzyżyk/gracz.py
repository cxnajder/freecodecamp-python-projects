class Gracz:
    def __init__(self, znak = 'o'):
        self.znak = znak
    
    def WyborPodpowiedź(self):
        print("Numery pól do wyboru:")
        print("+---" * 3 + "+") # da to samo co: print("+---+---+---+")
        for i in range(9):
            print(f"| {i + 1} ", end="")
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

class GraczCzłowiek (Gracz):
    def __init__(self, znak):
        super().__init__(znak)
            
    def Wybor(self):
        while True:
            try:
                wybrana_liczba = int(input("Wybierz pole (1-9): "))
                assert 1 <= wybrana_liczba <= 9, "Niewłaściwy zakres"
                poziom = (wybrana_liczba - 1) // 3
                pion = (wybrana_liczba - 1) % 3
                return (self.znak, poziom, pion)
            except ValueError:
                print("Niwłaściwy input")
            except AssertionError:
                print("Wybór z poza zakresu")
                self.WyborPodpowiedź()
    
import random

class GraczKomp (Gracz):
    def __init__(self, znak='o'):
        super().__init__(znak)

    def Wybor(self, lista_wolnych_pól = [i for i in range(1, 10)]):
        wybrana_liczba = random.choice(lista_wolnych_pól)
        print(f"Komputer wybrał pole {wybrana_liczba}")
        poziom = (wybrana_liczba - 1) // 3
        pion = (wybrana_liczba - 1) % 3
        return (self.znak, poziom, pion)

if __name__ == "__main__":
    gracz1 = GraczCzłowiek('x')
    gracz1.WyborPodpowiedź()
    print(gracz1.Wybor())

    gracz2 = GraczKomp('o')
    print(gracz2.Wybor())