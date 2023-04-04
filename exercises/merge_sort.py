def merge(T, S):
    n = len(T)
    m = len(S)
    start_1st = 0
    start_2nd = 0
    output = [0] * (n + m)
    current_idx = 0
    while start_1st < n and start_2nd < m:
        if T[start_1st] < S[start_2nd]:
            output[current_idx] = T[start_1st]
            start_1st += 1
        else:
            output[current_idx] = S[start_2nd]
            start_2nd += 1
        current_idx += 1
    while start_1st < n:
        output[current_idx] = T[start_1st]
        start_1st += 1
        current_idx += 1
    while start_2nd < m:
        output[current_idx] = S[start_2nd]
        start_2nd += 1
        current_idx += 1
    return output


def merge_sort(T, start, end):
    n = end - start
    if n <= 0:
        return [T[start]]
    middle = start + n // 2
    left = merge_sort(T, start, middle)
    right = merge_sort(T, middle + 1, end)
    return merge(left, right)


array = [3, 4, 5, 6, 1, 2, 0, 1]
big_array = [6903, 3826, 859, 6941, 1717, 4641, 8439, 5145, 2508, 6953, 1511, 9901, 6101, 4651, 4981, 5533, 7208, 9572, 6719, 8105, 4610, 8740, 4843, 2256, 3112, 6388, 267, 702, 8204, 4858, 1572, 1807, 765, 3615, 5115, 4367, 7533, 3002, 4732, 6713, 4084, 1890, 7361, 9112, 1097, 3508, 9536, 1369, 2063, 2799, 6768, 1636, 6253, 2845, 3108, 234, 8555, 6097, 5991, 5318, 767, 1192, 1612, 8242, 1873, 6251, 4477, 9509, 753, 4246, 6448, 8477, 9185, 7915, 7816, 2499, 8726, 9695, 5883, 2998, 7700, 7346, 3219, 9977, 7875, 5726, 8076, 9292, 5074, 5505, 2035, 423, 9982, 511, 1786, 3999, 1211, 351, 7722, 1842, 2766, 4740, 386, 6410, 6283, 6966, 4236, 9966, 4957, 1290, 1451, 1313, 6630, 2430, 3389, 6477, 4410, 991, 9540, 7072, 4469, 7770, 3066, 3943, 7849, 8873, 5702, 6661, 2461, 6855, 5817, 9902, 3678, 5434, 250, 6386, 5262, 6616, 9776, 4961, 5328, 8919, 2426, 8303, 8672, 4689, 4781, 5255, 8858, 2900, 6881, 5357, 5415, 1054, 3236, 7623, 1142, 258, 5473, 7134, 9194, 4926, 3378, 1990, 3778, 3693, 3760, 3150, 8480, 4544, 1161, 768, 5169, 2758, 6516, 3360, 6910, 2881, 8090, 3248, 517, 1240, 2919, 9691, 9869, 9886, 6831, 8513, 4292, 7341, 2582, 2593, 8971, 8879, 662, 4548, 671, 5687, 691, 2054]

sorted_big_array = merge_sort(big_array, 0, len(big_array) - 1)
# print(sorted_big_array)

big_array.sort()

for idx in range(0, len(big_array)):
    if big_array[idx] != sorted_big_array[idx]:
        print("WRONG")
