# liczby ze zbioru [0, n^2 - 1], jest ich n
# sortujemy je w czasie liniowym


def q_sort(T):
    n = len(T)
    C = [0] * n
    for x in T:
        C[x % n] += 1
    for x in range(1, n):
        C[x] = C[x - 1] + C[x]
    B = [0] * n
    for x in range(n - 1, -1, -1):
        B[C[T[x] % n] - 1] = T[x]
        C[T[x] % n] -= 1
    C = [0] * n
    for x in T:
        C[x // n] += 1
    for x in range(1, n):
        C[x] = C[x] + C[x - 1]
    W = [0] * n
    for x in range(n - 1, -1, -1):
        W[C[B[x] // n] - 1] = B[x]
        C[B[x] // n] -= 1
    return W