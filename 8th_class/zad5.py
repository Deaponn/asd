# problem przewodnika turystycznego (6th_class, zad4)

# przewodnik chce przewiezc grupe k turystow z miasta A do miasta B
# po drodze jednak jest wiele innych miast (wierzcholkow)
# miedzy wszystkimi miastami jezdza autobusy (krawedzie)
# mamy zadana liste trojek (x, y, c)
# ktore mowia (pierwsze miasto, miasto docelowe, ile osob moze przejechac na raz)
# np. (3, 6, 17) - z miasta 3 do 6 moze przejechac 17 osob

# przewodnik musi podzielic turystow na takie grupy, 
# zeby mogly one przejechac dana trasa w calosci (wszystkie grupy maja te sama trase)

# graf zadany jest jako lista krawedzi

# zaproponuj algorytm zwracajacy ilosc grupek, na ktore przewodnik podzieli k osob

# sortujemy krawedzie malejaco
# dokladamy do FindUnion do momentu gdy A i B beda w tym samym zbiorze