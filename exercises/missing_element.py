# Na wejsciu mamy posortowany ciąg liczb całkowitych A = {a_0, ..., a_n-1}
# z zakresu od 0 do m-1. Liczby w ciągu są parami różne. Co więcej n < m. 
# Proszę podać algorytm który znajduje najmniejszą liczbę całkowitą, której nie ma w A

# linear solution:
def find_missing_linear(T):
    missing = 0
    for x in T:
        if x != missing:
            return missing
        missing += 1
    return len(T)

# It works because if a number under given index is bigger than the index,
# then it means there is a number to the left missing (1), because the index is too small for this number
# Else, if index is equal to the number under the index,
# there must be a number to the right missing (2) since we know for certain that SOME number must be missing
# In these two scenarios, we move the searched range of indexes to be the 
# (1) left half of the range
# (2) right half of the range

# logn solution:
def find_missing_log(T):
    n = len(T)
    start = 0
    end = n
    while start != end:
        middle = start + (end - start) // 2
        if middle < T[middle]:
            end = middle
        else:
            start = middle + 1
    return start

print(find_missing_linear([0,1,2,3,4,6,7,8,9]))
print(find_missing_linear([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]))
print(find_missing_linear([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(find_missing_linear([0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]))
print(find_missing_log([0,1,2,3,4,6,7,8,9]))
print(find_missing_log([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]))
print(find_missing_log([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(find_missing_log([0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]))