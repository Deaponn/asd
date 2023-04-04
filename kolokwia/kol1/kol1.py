# Bartosz Sajecki

# algorytm przechodzi przez wszystkie przedzialy ktore rozwazamy na potrzeby zadania
# w tych przedzialach znajduje k-ta najwieksza liczbe za pomoca funkcji select
# zlozonosc tego algorytmu to O(np)


from kol1testy import runtests


def partition(T, start, end):
    pivot = T[end - 1]
    last_biggest = start
    for x in range(start, end - 1):
        if T[x] >= pivot:
            T[last_biggest], T[x] = T[x], T[last_biggest]
            last_biggest += 1
    T[last_biggest], T[end - 1] = T[end - 1], T[last_biggest]
    return last_biggest


def quick_select(T, start, end, looking_for):
    found_idx = partition(T, start, end)
    if found_idx == looking_for:
        return found_idx
    if found_idx < looking_for:
        return quick_select(T, found_idx + 1, end, looking_for)
    else:
        return quick_select(T, start, found_idx, looking_for)


def ksum(T, k, p):
    n = len(T)
    fragment = T[:p]
    quick_select(fragment, 0, p, k - 1)
    output = fragment[k - 1]
    for next_idx in range(p, n):
        next_item = T[next_idx]
        prev_item = T[next_idx - p]
        for idx in range(0, p):
            if fragment[idx] == prev_item:
                fragment[idx] = next_item
                break
        quick_select(fragment, 0, p, k - 1)
        output += fragment[k - 1]
    return output


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
