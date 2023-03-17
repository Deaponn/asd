# majac tablice n liczb rzeczywistych
# jest ona k-chaotyczna, czyli
# po posortowaniu tej tablicy indeks kazdego elementu zmieni sie maksymalnie o k

# napisz algorytm sortujacy podana tablice, mozliwie jak najszybciej

# najlepszy jest insertion sort, poniewaz najwiecej przeniesien elementu (w lewo) bedzie k
# zlozonosc to O(n)

# a) k = O(1), zlozonosc to n
# b) k = O(log n), zlozonosc to n log n, ale da sie to zrobic w n log(log n)

# sortuje pierwsze k elementow budujac z nich kopiec, a potem
# do tego samego kopca wstawiam kazdy nastepny element i usuwam pierwszy (najmniejszy)