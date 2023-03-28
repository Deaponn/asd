def left(n):
    return 2 * n + 1

def right(n):
    return 2 * n + 2

def parent(n):
    return (n - 1) // 2

def heapify(T, i, n):
    max_element_idx = i
    left_child = left(i)
    right_child = right(i)
    if left_child < n and T[left_child] > T[max_element_idx]:
        max_element_idx = left_child
    if right_child < n and T[right_child] > T[max_element_idx]:
        max_element_idx = right_child
    if max_element_idx != i:
        T[i], T[max_element_idx] = T[max_element_idx], T[i]
        heapify(T, max_element_idx, n)

def build_heap(T):
    n = len(T)
    for idx in range(parent(n - 1), -1, -1):
        heapify(T, idx, n)


def heapsort(T):
    n = len(T)
    build_heap(T)
    last_unsorted_idx = n - 1
    while last_unsorted_idx > 0:
        T[0], T[last_unsorted_idx] = T[last_unsorted_idx], T[0]
        heapify(T, 0, last_unsorted_idx)
        last_unsorted_idx -= 1


array = [0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9]

heapsort(array)

print(array)