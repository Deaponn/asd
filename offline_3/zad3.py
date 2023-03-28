# Bartosz Sajecki

# program dziala, poniewaz dubluje kazde slowo od tylu, za wyjatkiem palindromow
# dzieki temu wystarczy posortowac tablice i policzyc ile razy to samo slowo wystapilo pod rzad
# co policzy pierwotne slowa w dobra strone, i te ktore od tylu wygladaly tak samo
# np.
# [tok, auto, kot, kot, kajak] zostanie zamienione na
# [tok, auto, kot, kot, kajak, kot, otua, tok, tok] a nastepnie posortowane do postaci
# [auto, kajak, kot, kot, kot, otua, tok, tok, tok]


from zad3testy import runtests


LETTERS = 26
ASCII_OFFSET = 97


def counting_sort(T, comparison_index):
    n = len(T)
    letters = [0] * LETTERS
    output = [0] * n
    for i in range(n):
        idx = 0
        if comparison_index < len(T[i]):
            idx = ord(T[i][comparison_index]) - ASCII_OFFSET
        letters[idx] += 1
    for i in range(1, LETTERS):
        letters[i] += letters[i - 1]
    for idx in range(n - 1, -1, -1):
        working_char = 0
        if comparison_index < len(T[idx]):
            working_char = ord(T[idx][comparison_index]) - ASCII_OFFSET
        output[letters[working_char] - 1] = T[idx]
        letters[working_char] -= 1
    return output
    

def radix_sort(T, longest):
    output = counting_sort(T, longest)
    for length in range(longest - 1, -1, -1):
        output = counting_sort(output, length)
    return output


def strong_string(T):
    for idx in range(len(T)):
        word = T[idx]
        if word[::-1] != word:
            T.append(word[::-1])
    max_length = len(max(T, key = lambda word: len(word)))
    if max_length > 100:
        max_length = 100
    # sorted_array = radix_sort(T, max_length)
    sorted_array = T
    strongest = 0
    current = 1
    for idx in range(0, len(sorted_array) - 1):
        if sorted_array[idx] == sorted_array[idx + 1]:
            current += 1
        else:
            if strongest < current:
                strongest = current
            current = 1
    return strongest


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
