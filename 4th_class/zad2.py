# tablica A o dlugosci n
# wartosci tej tablicy sa calkowite z pewnego zbioru B, |B| = logn

# A = [8, 17, 31, 4, 8, 4]
# T - tablica bez powtorek
# L - tablica licznikow
# szukamy czy liczba jest obecna za pomoca binary search, zlozonosc log(logn), bo tyle mamy liczb
# nowa liczbe wstawiamy od razu na miejsce, w razie potrzeby przesuwajac wszystko w prawo, zlozonosc log^2(n)
# T = [4, 8, 17, 31]
# L = [2, 2, 1, 1]

# quicker sort, sortujacy na mniejsze, rowne, wieksze
# daje to log(logn)

