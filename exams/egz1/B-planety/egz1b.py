# Bartosz Sajecki

# zalozenie o pustym zbiorniku paliwa niezbednym do teleportacji mozna pominac tankujac zawsze na styk przed przelotem
# wtedy po doleceniu na planete po drodze, zawsze mozna skorzystac z teleportacji
# lub druga sytuacja, gdy paliwo jest tanie to mozna tankowac do pelna
# nic pomiedzy sie nie oplaca:
# ani tankowanie drogiego paliwa wiecej niz na styk
# ani tankowanie taniego paliwa do pelna gdy na nastepnej planecie jeszcze taniej skorzystamy z teleportacji

# b - ilosc paliwa w baku
# niech d(i, j) = D[j] - D[i] - dystans miedzy planetami i oraz j
# niech c(i, j, b) = min((d(i, j) - b) * C[i] if d(i, j) <= E else +inf, T[i][1] if T[i][0] == j and b == 0 else +inf) - koszt przelotu 
# miedzy planetami i oraz j, w lewej czesci funkcji min obliczany jest koszt paliwa, a w prawej koszt teleportacji
# f(i, b) = |N - funkcja zwracajaca minimalny koszt przelotu na planete i z planety 0, gdy w baku jest b ton paliwa
# f(n - 1, 0) = rozwiazanie
# f(0, 0) = 0
# f(1, b) = min(cost(0, 1, b), cost(0, 1, d(0, 1)) + (d(0, 1) - b) * C[0])
# f(2, b) = min(cost(0, 2, b), f(0, 1, b) + cost(1, 2, b))
# f(3, b) = min(f(0, 3, b), f(1, 3, b) + cost(1, 3, b), f(0, 2, b) + cost(2, 3, b))
# f(i, b) = min(c(0, i), f(x, 0) + c(x, i) for x in range(i))

# doleciec na i-ta planete moge potencjalnie z kazdej poprzedniej planety, uzywajac jej jako "przystanek"

from egz1btesty import runtests


def distance(i, j, D):
    return D[j] - D[i]


def tp_cost(i, j, fuel, T):
    return T[i][1] if T[i][0] == j and fuel == 0 else float("inf")


def flight_cost(i, j, fuel, max_fuel, D, C):
    return (distance(i, j, D) - fuel) * C[i] if distance(i, j, D) <= max_fuel else float("inf")


def planets( D, C, T, E ):
    # tu prosze wpisac wlasna implementacje
    n = len(D)
    lowest_costs = [float("inf")] * n
    lowest_costs[0] = 0
    for reach in range(1, n):
        for previous in range(0, reach):
            # print("analyzing", reach, "against", previous, lowest_costs[previous], tp_cost(previous, reach, 0, T), flight_cost(previous, reach, 0, E, D, C))
            prev_to_reach_travel_cost = lowest_costs[previous] + min(tp_cost(previous, reach, 0, T), flight_cost(previous, reach, 0, E, D, C))
            if lowest_costs[reach] > prev_to_reach_travel_cost:
                # print("cheaper reach", lowest_costs[reach], prev_to_reach_travel_cost)
                lowest_costs[reach] = prev_to_reach_travel_cost
    return lowest_costs[n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
