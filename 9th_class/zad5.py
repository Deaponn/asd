# graf wazony nieskierowany
# trzeba znalezc maksymalny przeplyw od zadanych wierzcholkow od s do t

# mamy podany algorytm dzialajacy dla grafu skierowanego

# zmieniamy graf nieskierowany na skierowany

# rozdzielamy krawedz stawiajac na niej wierzcholek o tej samej wadze co wejsciowa krawedz
# i laczymy wierzcholki wstecz z taka sama waga
# dzieki temu graf nie ma zbyt malych petli i algorytm sie nie wywali

# A----5--->B

#      | 
#      | 
#      | 
#      v 

#   ______5_______
#  /             \/
# A---5-->o---5-->B