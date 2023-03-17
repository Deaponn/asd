# struktura danych pozwalajaca w czasie logarytmicznym dodac element oraz usunac mediane
# jesli dlugosc tablicy jest parzysta, to zwracamy srednia z dwoch elementow i usuwamy oba

# mediane trzymamy na szczycie kopca
#          5 mediana
#     min heap   max heap
#        _2_       _7_
#       /   \     /   \
#      1     3   6     10

# jesli nowy element jest wiekszy od 5, wkladamy go do max heap
# wtedy najmniejszy element z max heap przechodzi do mediany

#          5, 6 mediana
#     min heap   max heap
#        _2_        7_
#       /   \         \
#      1     3        10
#                       \
#                       11

# jesli mniejszy, to wkladamy nowy element do min heap
# wtedy najwiekszy element z min heap przenosze do mediany

# gdy dojda dwa wieksze elementy niz mediana, to przekladamy mediane do min heap
# najmniejszy element z max heap staje sie mediana, a do max heap dodajemy oba elementy

# przy usuwaniu elementu przenosimy mediane i robimy heapify na kopcach