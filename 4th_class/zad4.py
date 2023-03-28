# majac slowa A i B, kazde o dlugosci n
# ilosc liter w alfabecie = k
# mamy sprawdzic w czasie n + k, czy te slowa to anagramy
# dodajemy na odpowiedni indeks wedlug litery + 1, potem odejmujemy
# na koncu sprawdzamy czy wszedzie jest 0

# w czasie O(n)
# inicjalizujemy tablice, ale nie ustawiajac wszystkiego na 0 (ze smieciami)
# przechodzimy po obu slowach i ustawiamy 0
# przechodzimy drugi raz i robimy +1
# przechodzimy trzeci raz i robimy -1
# przechodzimy czwarty i sprawdzamy czy wszedzie sa 0
# w ten sposob nie tracimy czasu na inicjalizowanie tablicy zerami na miejscu liter, ktore nawet nie wystepuja w tych slowach
# ma to znaczenie przy bardzo duzym alfabecie
