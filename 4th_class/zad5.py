# mamy tablice n liczb
# znajdz dwie liczby x, y
# takie, ze x - y jest najwieksza i nie istnieje z: y < z < x
# zlozonosc nlogn - posortowac i znalezc dwie sasiadujace liczby o najwiekszej roznicy
# da sie O(n)
# szukamy odwroconego min i max????
# A = [5, 6, 7, 1, 2, 3, 5]
# dzielimy tablice na n kubelkow
# n = max - min (oba znalezione w czasie liniowym)
# przechodzimy po kubelkach i do innej tablicy przepisujemy min i max kazdego kubelka
# tablica ta jest posortowana
# potem przechodzimy do tej tablicy i znajdujemy najwieksza roznice