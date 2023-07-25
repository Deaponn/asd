# ladowanie promu

# prom ma dwa pasy na ktorych przewiezc mozna pojazdy
# auta wjezdzaja na prom pojedynczo czekajac w kolejce
# auto moze wjechac na lewy lub prawy pas i dojezdza az pocaluje auto przed nim
# tablica A[0..n-1] zawiera dlugosci samochodow
# majac dane L jako dlugosc promu, obliczyc ile maksymalnie aut zmiesci sie na promie

# f(i, s) - maksymalna liczba aut, ktore moga wjechac na prom, 
# jesli znajduja sie na nim auta od 0 do i oraz zajmuja s na lewym pasie

# f(i, s) = max(f(i + 1, s + a_i+1) + 1, f(i + 1, s) + 1, i) - i w przypadku gdy auto nie wjezdza na prom
# f(i, s) = -inf gdy s > L lub (suma dlugosci aut od auta 0 do i) - s > L (mozemy obliczyc dlugosc aut na prawym pasie)