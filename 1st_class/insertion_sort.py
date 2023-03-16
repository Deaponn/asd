# create insertion sort algorithm
def sort(T):
    n = len(T)
    for x in range(n):
        for offset in range(x - 1, -1, -1):
            if T[offset] > T[offset + 1]:
                T[offset + 1], T[offset] = T[offset], T[offset + 1]
            else:
                break
    return T

list =  [4, 0, 3, 10, 3, 6, 7, 8, 2]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(sort(list))
print("\n")
print(sort(list2))