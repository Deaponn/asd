# Bartosz Sajecki

from zad1testy import runtests

# funkcja przechodzi po kazdym elemencie tablicy zakladajac,
# ze ten element jest srodkiem palindromu;
# analizowane sa dwie pozycje jednoczesnie, jedna jako srodek palindromu w lewej czesci slowa,
# druga jako srodek w prawej czesci slowa;
# nastepnie rozszerza palindrom w lewo i prawo porownujac znaki;
# jesli znaki sa takie same, to zwieksza dlugosc znalezionego palindromu;
# przestaje szukac wiekszych palindromow gdy napotka rozne znaki na pozycji, na ktorej palindrom mialby te same znaki;
# jesli dlugosc znalezionego palindromu bedzie wieksza niz liczba znakow,
# ktore pozostaly do konca slowa, to jest to najdluzszy palindrom i funkcja zwraca jego dlugosc;
# jest tak, poniewaz palindromy szukane sa od srodka;
# zlozonosc tego algorytmu to n^2

def ceasar( s ):
    n = len(s)
    max_size = 0
    right_center = n // 2
    left_center = right_center - 1
    if n % 2 == 1:  # sprawdzenie sytuacji gdy srodek palindromu jest w samym srodku slowa
        right_center += 1   # poprawienie pozycji prawego centrum, na potrzeby dalszej czesci algorytmu
        center = n // 2
        size = 1
        while center + size < n and s[center - size] == s[center + size]:
            size += 1
        max_size = size
    
    for _ in range(0, n - 1):
        left_palindrome_valid = True
        right_palindrome_valid = True
        size = 1
        while left_center - size > -1:  # wystarczy sprawdzac czy nie wyszlismy poza slowo z lewej, poniewaz z prawej sytuacja jest lustrzana
            if left_palindrome_valid and s[left_center - size] != s[left_center + size]:
                left_palindrome_valid = False
            if right_palindrome_valid and s[right_center - size] != s[right_center + size]:
                right_palindrome_valid = False
            if not left_palindrome_valid and not right_palindrome_valid:
                break
            size += 1
        if size > max_size:
            max_size = size
        if max_size - left_center > -1:
            return max_size * 2 - 1
        left_center -= 1
        right_center += 1
    return max_size * 2 - 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = False )
