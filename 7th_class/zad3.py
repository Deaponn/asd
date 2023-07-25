# iloczyn wag
# mamy graf z wagami |R+
# chcemy znalezc sciezke, ktorej iloczyn segmentow jest najmniejszy
# nie mozemy tego robic dijkstra z mnozeniem, bo blad na liczbie zmiennopozycyjnej spowoduje zmiane dlugosci sciezki
# trzeba zlogarytmowac te liczby i potem je dodawac
# potem, poniewaz logarytm moze byc ujemny to stosujemy algortym Bellmana-Forda