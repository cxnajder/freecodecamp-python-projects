import gracz

class Gra:
    def __init__(self):
        self.plansza = [[" " for i in range(3)] for j in range(3)]

    def pokazPlansze(self):
        print("+---" * 3 + "+") # da to samo co: print("+---+---+---+")
        for i in range(3):
            print("|", end='')
            for j in range (3):
                print("", self.plansza[i][j], "|", end="")
            print()
            print("+---" * 3 + "+") # da to samo co: print("+---+---+---+")
            # +---+---+---+
            # |   |   |   |
            # +---+---+---+
            # |   | o |   |
            # +---+---+---+
            # |   |   | x |
            # +---+---+---+
    
    def czyJestMiejsce(self):
        for i in self.plansza:
            for j in i:
                if j == " ":
                    return True
        return False

    def wolnePola(self):
        lista_pol = []
        for i in range(1,10):
            poziom = (i - 1) // 3
            pion = (i - 1) % 3
            if self.plansza[poziom][pion] == " ":
                lista_pol.append(i)
        return lista_pol


    def ustawPole(self, znak, poziom, pion):
        # poziom - index y
        # pion   - index x
        try:
            assert self.plansza[poziom][pion] == " ", f"Pole jest już zajęte przez \'{self.plansza[poziom][pion]}\'"
            self.plansza[poziom][pion] = znak
        except IndexError:
            print("Niewłaściwy index --- plansza[0-2][0-2]")
            raise
        except AssertionError:
            print("Pole jest już zajęte")
            raise
    
    def zajetePrzezO(self):
        zajepte_pola = []
        for i in range(1,10):
            poziom = (i - 1) // 3
            pion = (i - 1) % 3
            if self.plansza[poziom][pion] == 'o':
                zajepte_pola.append(i)
        return zajepte_pola

    def czyJestZwyciezca(self, znak):
        for i in range(3):
            if self.plansza[i][0] == znak and self.plansza[i][1] == znak and self.plansza[i][2] == znak:
                return True
            if self.plansza[0][i] == znak and self.plansza[1][i] == znak and self.plansza[2][i] == znak:
                return True
            if self.plansza[0][2] == znak and self.plansza[1][1] == znak and self.plansza[2][0] == znak:
                return True
            if self.plansza[0][0] == znak and self.plansza[1][1] == znak and self.plansza[2][2] == znak:
                return True
        return False

    def rozpocznijGre(self, tryb_gry = 1):
        assert tryb_gry in [1, 2, 3] # dostepne są tylko 3 tryby gry!
        match tryb_gry:
            case 1:
                self.gracz1 = gracz.GraczCzlowiek('o')
                self.gracz2 = gracz.GraczKomp('x')
            case 2:
                self.gracz1 = gracz.GraczCzlowiek('o')
                self.gracz2 = gracz.GraczCzlowiek('x')
            case 3:
                self.gracz1 = gracz.GraczKomp('o')
                self.gracz2 = gracz.GraczKomp('x')
        
        self.plansza = [[" " for i in range(3)] for j in range(3)] # wyczyszczenie planszy (na wszelki wypadek)

        rozgrywajacy = self.gracz2
        self.zwyciezca = None
        numer_gracz_z_tura = 1
        rozgrywajacy.WyborPodpowiedz()

        while(self.czyJestMiejsce()):
            if rozgrywajacy == self.gracz2:
                rozgrywajacy = self.gracz1
            else:
                rozgrywajacy = self.gracz2

            udany_wybor = False
            while not udany_wybor:
                try:
                    print(f"Gracz {numer_gracz_z_tura}: ", end = "")
                    znak, poziom, pion = rozgrywajacy.Wybor(self.wolnePola())
                    self.ustawPole(znak, poziom, pion)
                    udany_wybor = True
                except AssertionError:
                    rozgrywajacy.WyborPodpowiedz(self.wolnePola(), self.zajetePrzezO())
                    print("Spróbuj jeszcze raz")
            self.pokazPlansze()
            if self.czyJestZwyciezca(rozgrywajacy.znak):
                self.zwyciezca = rozgrywajacy.znak
                break
            numer_gracz_z_tura = numer_gracz_z_tura % 2
            numer_gracz_z_tura += 1

        if self.zwyciezca == None:
            print("Remis")
        else:
            print(f"Wygrywa gracz numer {numer_gracz_z_tura} (używający \'{self.zwyciezca}\')")

def tik_tak_toe():
    nowaGra = Gra()

    # MENY:
    print("+" * 40)
    print("| 1) "+"Gracz vs CPU".center(30)+"    |")
    print("| 2) "+"Gracz vs Gracz".center(30)+"    |")
    print("| 3) "+"CPU vs CPU".center(30)+"    |")
    print("+" * 40)
    
    poprawnyWybor = False
    while not poprawnyWybor:
        try:
            opcja = int(input("Wybierz opcje z zakresu (1-3): "))
            assert 1 <= opcja <= 3
            poprawnyWybor = True
        except AssertionError:
            print("Opcja z poza zakresu")
        except ValueError:
                print("Niwłaściwy input")

    nowaGra.rozpocznijGre(opcja)

if __name__ == "__main__":

    tik_tak_toe()