# qiven a following stack API:
# stack.push(x)
# x = stack.pop()
# stack.is_empty()
# implement non-recursive quick sort


class Stack:
    def push(x):
        return x
    def pop():
        return 1
    def is_empty():
        return False


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r - 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r - 1] = arr[r - 1], arr[i + 1]
    return i + 1


def quick_sort(arr, p, r):
    stack = Stack()
    stack.push((p, r))
    while not stack.is_empty():
        p, r = stack.pop()
        q = partition(arr, p, r)
        if p < q - 1:
            stack.push((p, q))
        if q + 1 < r:
            stack.push((q + 1, r))