# graf ma spojnosc krawedziowa k, jesli po usunieciu k krawedzi stanie sie niespojny

# wybieramy wierzcholki na zrodlo i ujscie
# szukamy krawedzi po ktorych przecieciu podzielimy graf na dwie spojne skladowe gdzie
# zrodlo nalezy do jednej spojnej, a ujscie do drugiej
# i suma wag tych krawedzi jest minimalna

# wybieramy wierzcholek ktory zawsze jest zrodlem i potem dla kazdego innego wierzcholka sprawdzamy
# jakby byl zrodlem i sprawdzam przeplyw miedzy nimi szukajac minimum