# graf skierowany z poczatkiem i koncem (s i t)
# szukamy maksymalna liczbe sciezek rozlacznych wierzcholkowo z s do t

# po przejsciu wierzcholkiem powinnismy blokowac ten wierzcholek

# kazdy wierzcholek rozdzielamy na dwa wierzcholki:
# wierzcholek A, do ktorego wpadaja krawedzie ze starego wierzcholka
# wierzcholek B, do ktorego jest krawedz wagi 1 od wierzcholka A i z ktorego wychodza wszystkie krawedzie z wyjsciowego wierzcholka

# dzieki temu przeplyw przez wierzcholek wynosi 1, i tylko jedna krawedz wchodzaca i wychodzaca bedzie miala przeplyw 1

# za pomoca maksymalnego przeplywu szukamy maksymalnej ilosci krawedzi do przeciecia od wierzcholkow A_i do B_i