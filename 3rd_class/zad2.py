# struktura danych pozwalajaca zwrocic najmniejszy, zwrocic najwiekszy i dodac nowy element
# wszystkie operacje w czasie log n
# i usuwac elementy w czasie liniowym

# dla liczb 5, 3, 7, 1, 10, 2, 6
# tworzymy kopiec
#           ___10___
#          /        \
#        _7_        _6_
#       /   \      /   \
#      5     3    1     2
# z takiej struktury odczyt najwiekszego elementu jest realizowany w czasie log n
# aby wstawic element, doczepiamy go i wykonujemy naprawianie kopca
# aby odczytac najmniejszy element, tworzymy kopiec odwrotny
#           ___1___
#          /        \
#        _3_        _2_
#       /   \      /   \
#      5     7    9     6
#      |
#      10
# nowy element dodajemy do obu kopcow
# tak samo jak usuwamy stary element z obu kopcow
# aby usprawnic usuwanie elementu, przechowujemy krotki (value, index_in_opposite_heap)
# usuwajac element z "wiekszego" kopca, naprawiamy go funkcja heapify
# indeks usuwanego elementu usuwamy z "najmniejszego" kopca
# a nastepnie przesuwamy elementy, aby "zalepic" dziure