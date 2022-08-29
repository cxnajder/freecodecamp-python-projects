import random 

def play():
    user = input("""k - kamień
p - papeir
n - nożyczki
>>""")
    computer = random.choice(['k', 'p', 'n'])

    if user == computer:
        return "Remis"
    if winner(user, computer):
        return "Wygrałeś"
    return "Przegrałeś"

# k > n | n > p | p > k

def winner(gracz, przeciwnik):
    if (gracz == 'k' and przeciwnik == 'n') or (gracz == 'n' and przeciwnik == 'p') or (gracz == 'p' and przeciwnik == 'k'):
        return True


print(play())