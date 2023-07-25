# panstwo, w ktorym jest n miast postanowiono zbudowac autostrady
# chcemy te miasta polaczyc siatka autostrad, ktore uczynia to panstwo grafem spojnym
# polozenie kazdego miasta opisuja wspolrzedne x, y
# a odleglosc od miast jest odlegloscia euklidesowa
# zaproponuj algorytm ktory zminimalizuje czas miedzy otwarciem pierwszej a ostatniej autostraady
# czas budowy autostrady wynosi ceil(length), w kilometrach

# budujemy minimalne drzewo rozpinajace za pomoca Kruskalla
# liczymy rozpietosc czasu budowy
# po zbudowaniu usuwamy najkrotsza droge i odbudowujemy drzewo dalszymi, dluzszymi autostradami
# liczymy rozpietosc czasu budowy
# i tak w kolko szukajac najmniejszej wartosci