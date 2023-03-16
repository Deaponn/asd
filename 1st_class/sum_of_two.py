# T is sorted array, x is a number
# find two indexes, i and j, such that T[i] - T[j] = x

# we start with i = 0 and j = 1
# in every step we compute T[i] - T[j]
# if this is more than x, we need to increment i, so the difference between T[i] and T[j] is smaller
# if this is less than x, we need to increment j, so the difference between T[i] and T[j] is bigger
# this works (if the pair of numbers exist), because we can't "walk" our indexes out of the solution scope, ex.:
# given T = [2, 4, 5, 1, 6, 9, 10] and x = 10
# we can't end up here:
#     i           j
#     |           |
#     v           v
# [2, 4, 5, 1, 6, 9, 10]
# because that means we were here in the previous step
#     i        j
#     |        |
#     v        v
# [2, 4, 5, 1, 6, 9, 10]
# this is due to the fact that we move only one pointer at the time
# simirarily, we can't end up in this position:
#        i     j
#        |     |
#        v     v
# [2, 4, 5, 1, 6, 9, 10]
# because that means we were here in the previous step
#     i        j
#     |        |
#     v        v
# [2, 4, 5, 1, 6, 9, 10]
# this is due to the fact that we move only one pointer at the time


# def find_indexes(T, x):
# solution TBD