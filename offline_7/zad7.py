# Bartosz Sajecki

# korzystajac z funkcji:
# f(x, y), ktora zwraca maksymalna liczbe komnat odwiedzonych od rogu [0, 0]
# do komnaty o koordynatach [x, y], mozna obliczyc wartosci dla calej macierzy
# a nastepnie zwrocic f(n - 1, n - 1)

# direction - kierunek z ktorego przyszlismy (2 - z gory, 1 - z lewej, 0 - z dolu)
# f(x, y, direction) = {
#               -infinity, gdy L[x][y] == "#" lub y > n - 1 lub x > n - 1
#               1, gdy x = y = n - 1
#               max(f(x, y - 1, 0), f(x + 1, y, 2)) + 1, gdy direction = 0
#               max(f(x, y - 1, 0), f(x, y + 1, 0), f(x + 1, y, 2)) + 1, gdy direction = 1
#               max(f(x, y + 1, 2), f(x + 1, y, 1)) + 1, gdy direction = 2
#           }


from zad7testy import runtests

def maze( L ):
    ########################## tail recursion:
    # n = len(L)
    # neg_inf = -float("inf")
    # output = [[[None] * 3 for _ in range(n)] for _ in range(n)]
    # output[n - 1][n - 1] = [0, 0, 0]
    # recursion_stack = [(0, 0, 2)]
    # while len(recursion_stack) > 0:
    #     x, y, direction = recursion_stack[-1]
    #     if not (0 <= x < n and 0 <= y < n):
    #         recursion_stack.pop()
    #         continue
    #     if L[y][x] == "#":
    #         output[y][x] = [neg_inf] * 3
    #         recursion_stack.pop()
    #         continue
    #     value = output[y][x][direction]
    #     if value is not None:
    #         recursion_stack.pop()
    #         continue
    #     if direction == 0:
    #         up = output[y - 1][x][0] if y > 0 else neg_inf
    #         right = output[y][x + 1][1] if x < n - 1 else neg_inf
    #         if up is not None and right is not None:
    #             value = max(up, right) + 1
    #             recursion_stack.pop()
    #         else:
    #             recursion_stack.append((x, y - 1, 0))
    #             recursion_stack.append((x + 1, y, 1))
    #     if direction == 1:
    #         up = output[y - 1][x][0] if y > 0 else neg_inf
    #         right = output[y][x + 1][1] if x < n - 1 else neg_inf
    #         down = output[y + 1][x][2] if y < n - 1 else neg_inf
    #         if up is not None and right is not None and down is not None:
    #             value = max(up, right, down) + 1
    #             recursion_stack.pop()
    #         else:
    #             recursion_stack.append((x, y - 1, 0))
    #             recursion_stack.append((x + 1, y, 1))
    #             recursion_stack.append((x, y + 1, 2))
    #     if direction == 2:
    #         right = output[y][x + 1][1] if x < n - 1 else neg_inf
    #         down = output[y + 1][x][2] if y < n - 1 else neg_inf
    #         if right is not None and down is not None:
    #             value = max(right, down) + 1
    #             recursion_stack.pop()
    #         else:
    #             recursion_stack.append((x + 1, y, 1))
    #             recursion_stack.append((x, y + 1, 2))
    #     output[y][x][direction] = value
    # return max([x if x is not None else -1 for x in output[0][0]])


    ########################## regular recursion:
    n = len(L)
    neg_inf = -float("inf")
    output = [[[None] * 3 for _ in range(n)] for _ in range(n)]
    output[n - 1][n - 1] = [0, 0, 0]
    def max_distance(x, y, direction):
        if not (0 <= x < n and 0 <= y < n) or L[y][x] == "#":
            return neg_inf
        value = output[y][x][direction]
        if value is not None:
            return value
        if direction == 0:
            value = max(max_distance(x, y - 1, 0), max_distance(x + 1, y, 1)) + 1
        if direction == 1:
            value = max(max_distance(x, y - 1, 0), max_distance(x, y + 1, 2), max_distance(x + 1, y, 1)) + 1
        if direction == 2:
            value = max(max_distance(x, y + 1, 2), max_distance(x + 1, y, 1)) + 1
        output[y][x][direction] = value
        return value
    max_distance(0, 0, 2)
    return max([x if x is not None else -1 for x in output[0][0]])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
