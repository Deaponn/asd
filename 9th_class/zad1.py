# w grafie skierowanym niektore wierzcholki to fabryki o mozliwosciach produkcji x jednostek towaru w jednostce czasu t
# krawedzie maja wagi o przepustowosci drog
# niektore wierzcholki to sklepy, maja one informacje o tym ile towaru sprzedaja w jednostce czasu
# czy da sie tak zaprojektowac siec transportowa aby kazdy sklep otrzymywal tyle towaru ile jest w stanie sprzedac?

# maksymalnego przeplywu szukamy miedzy wierzcholkiem wejsciowym ktory jest polaczony do fabryk
# a wierzcholkiem wyjsciowym polaczonym do sklepow

# waga krawedzi miedzy zrodlem a fabryka wynosi tyle ile produkuje fabryka
# waga krawedzi miedzy sklepem a ujsciem wynosi tyle ile sprzedaje sklep

# wykonujemy algorytm Forda-Fulkersona

# ilosci wplywow i ujsc musza byc takie same
# jesli beda sie roznic, to szukamy bledow w implementacji

# po wykonaniu algorytmu sprawdzamy czy wartosc przeplywu jest conajmniej taka jak suma potrzeb wszystkich sklepow