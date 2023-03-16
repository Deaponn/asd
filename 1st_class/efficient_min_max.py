# find min and max at the same time using 3/2 * n comparisons

# this works, because we compare k-th and (k+1)-th number,
# then we compare the lower one to min and the higher one to max,
# we make 3 comparisons for every pair of numbers, for a total of 3/2 * n
# as opposed to 2n comparisons if we use the naive approach, which would be
# to compare every number to min and then to max (2 comparisons for every number)
def min_max(T): 
    n = len(T)
    min_val = T[0]
    max_val = T[0]
    for idx in range(0, n, 2):
        if idx + 1 >= n:
            break
        if T[idx] < T[idx + 1]:
            if min_val > T[idx]:
                min_val = T[idx]
            if max_val < T[idx + 1]:
                max_val = T[idx + 1]
        else:
            if min_val > T[idx + 1]:
                min_val = T[idx + 1]
            if max_val < T[idx]:
                max_val = T[idx]
    return min_val, max_val


list =  [4, 0, 3, 10, 3, 6, 7, 8, 2]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(min_max(list))
print(min_max(list2))