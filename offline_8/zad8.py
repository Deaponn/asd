# Bartosz Sajecki

# jadac po jednej kratce, zbieram kazda plame paliwa
# gdy zauwaze, ze paliwo sie konczy, wybieram najwieksza z minietych plam
# i zakladam ze to wlasnie przy niej sie zatrzymalem
# wtedy pojemnosc tej plamy doliczam do calkowitego paliwa
# petle przerywam wczesniej gdy zauwaze,
# ze z obecnym paliwem moge dojechac na koniec trasy
# ale to pewnie niewiele daje
# zlozonosc tego rozwiazania to O(v^2*u*log(v))

from zad8testy import runtests
from queue import PriorityQueue



# 0 - gora, 1 - prawo, 2 - dol, 3 - lewo
def calculate_source_volume(x, y, origin, T):
    n = len(T)
    m = len(T[0])
    if T[y][x] == 0:
        return 0
    value = T[y][x]
    T[y][x] = 0
    up = calculate_source_volume(x, y - 1, 2, T) if y > 0 else 0
    right = calculate_source_volume(x + 1, y, 3, T) if x < m - 1 else 0
    down = calculate_source_volume(x, y + 1, 0, T) if y < n - 1 else 0
    left = calculate_source_volume(x - 1, y, 1, T) if x > 0 else 0
    if origin == 0:
        return value + right + down + left
    if origin == 1:
        return value + up + down + left
    if origin == 2:
        return value + up + right + left
    if origin == 3:
        return value + up + right + down


def ride(x, gas, gas_sources, memoized):
    m = len(gas_sources)
    if x + gas >= m - 1:
        return 0
    key = (x, gas)
    if key in memoized:
        return memoized[key]
    total_gas = gas + gas_sources[x]
    all_stops = [ride(x + distance, total_gas - distance, gas_sources, memoized) for distance in range(min(total_gas, m - x - 1), 0, -1)]
    if len(all_stops) == 0:
        return float("inf")
    output = min(all_stops) + 1
    memoized[key] = output
    return output


def plan(T):
    # iterative approach, very performant
    m = len(T[0])
    total_stops = 0
    total_gas = 0
    passed_gas_sources = PriorityQueue()
    for distance in range(m):
        gas_source = calculate_source_volume(distance, 0, 0, T)
        if gas_source > 0:
            passed_gas_sources.put(-gas_source)
        if total_gas - distance < 0:
            biggest_passed_source = -passed_gas_sources.get(block=False)
            total_gas += biggest_passed_source
            total_stops += 1
            if total_gas > m:
                return total_stops
    return total_stops

    
    # recursive approach, with memoization, preforming orders of magnitude slower than above
    # memoized = dict()
    # m = len(T[0])
    # gas_sources = [None] * m
    # for x in range(m):
    #     gas_sources[x] = calculate_source_volume(x, 0, 0, T)
    # output = ride(0, 0, gas_sources, memoized)
    # return output


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

