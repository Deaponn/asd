# quick sort variations for different time and space complexities


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
    # default quick sort
    # memory complexity n log n
    # if p >= r:
    #     return
    # q = partition(arr, p, r)
    # quick_sort(arr, p, q - 1)
    # quick_sort(arr, q, r)
    # end default quicksort

    # memory-performant quick sort
    # memory complexity n
    # while p < r:
    #     q = partition(arr, p, r)
    #     quick_sort(arr, p, q - 1)
    #     p = q + 1
    # end memory-performant quick sort

    # most-memory-performant quick sort
    # memory complexity log n
    # regular time complexity n log n, worst time complexity n^2
    while p < r:
        q = partition(arr, p, r)
        if q - p > r - q:
            quick_sort(arr, q - 1, r)
            r = q - 1
        else: 
            quick_sort(arr, p, q - 1)
            p = q + 1
    # end most-memory-performant quick sort