import gracz

class Gra:
    def __init__(self):
        self.plansza = [[" " for i in range(3)] for j in range(3)]

    def pokażPlanszę(self):
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
        lista_pól = []
        for i in range(1,10):
            poziom = (i - 1) // 3
            pion = (i - 1) % 3
            if self.plansza[poziom][pion] == " ":
                lista_pól.append(i)
        return lista_pól


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
    
    def czyJestZwycięzca(self):
                return False

    def rozpocznijGrę(self, tryb_gry = 1):
        assert tryb_gry in [1, 2, 3] # dostepne są tylko 3 tryby gry!
        match tryb_gry:
            case 1:
                self.gracz1 = gracz.GraczCzłowiek('o')
                self.gracz2 = gracz.GraczKomp('x')
            case 2:
                self.gracz1 = gracz.GraczCzłowiek('o')
                self.gracz2 = gracz.GraczCzłowiek('x')
            case 3:
                self.gracz1 = gracz.GraczKomp('o')
                self.gracz2 = gracz.GraczKomp('x')
        
        self.plansza = [[" " for i in range(3)] for j in range(3)] # wyczyszczenie planszy (na wszelki wypadek)

        rozgrywający = self.gracz2
        self.zwycięzca = None
        numer_gracz_z_turą = 1
        rozgrywający.WyborPodpowiedź()

        while(self.czyJestMiejsce()):
            if rozgrywający == self.gracz2:
                rozgrywający = self.gracz1
            else:
                rozgrywający = self.gracz2

            udany_wybór = False
            while not udany_wybór:
                try:
                    print(f"Gracz {numer_gracz_z_turą}: ", end = "")
                    match tryb_gry:
                        case 1: # gracz vs komp
                            match numer_gracz_z_turą: 
                                case 1: # tura gracza
                                    znak, poziom, pion = rozgrywający.Wybor()
                                case 2: # tura kompa
                                    znak, poziom, pion = rozgrywający.Wybor(self.wolnePola())
                        case 2: # gracz vs gracz
                            znak, poziom, pion = rozgrywający.Wybor()
                        case 3: # komp vs komp
                            znak, poziom, pion = rozgrywający.Wybor(self.wolnePola())
                    self.ustawPole(znak, poziom, pion)
                    udany_wybór = True
                except AssertionError:
                    rozgrywający.WyborPodpowiedź()
                    print("Spróbuj jeszcze raz")
            self.pokażPlanszę()
            if self.czyJestZwycięzca():
                if numer_gracz_z_turą == 1:
                    self.zwycięzca = 'o'
                else:
                    self.zwycięzca = 'x'
                break
            numer_gracz_z_turą = numer_gracz_z_turą % 2
            numer_gracz_z_turą += 1

        if self.zwycięzca == None:
            print("REMIS")
        else:
            print(f"Wygrywa gracz numer {numer_gracz_z_turą}, używający \'{self.zwycięzca}\'")

def tik_tak_toe():
    nowaGra = Gra()

    # MENY:
    print("+" * 40)
    print("| 1) "+"Gracz vs CPU".center(30)+"    |")
    print("| 2) "+"Gracz vs Gracz".center(30)+"    |")
    print("| 3) "+"CPU vs CPU".center(30)+"    |")
    print("+" * 40)
    
    poprawnyWybór = False
    while not poprawnyWybór:
        try:
            opcja = int(input("Wybierz opcje z zakresu (1-3): "))
            assert 1 <= opcja <= 3
            poprawnyWybór = True
        except AssertionError:
            print("Opcja z poza zakresu")
        except ValueError:
                print("Niwłaściwy input")

    nowaGra.rozpocznijGrę(opcja)

if __name__ == "__main__":

    tik_tak_toe()
    # nowaGra = Gra()
    # nowaGra.rozpocznijGrę()


    # print(nowaGra.gracz1)
    # print(nowaGra.gracz2)
    # print(nowaGra.zwycięzca)