# czarny las

# mamy tablice n-1 drzew, kazde z nich ma pewna wartosc (w C[i])
# chcemy sciac drzewa o jak najwiekszej wadze, nie mozemy scinac sasiednich drzew

# f(i, bool) - funkcja oznacza maksymalna wartosc scietych drzew od indeksu 0 do i oraz to czy scinamy drzewo i-te
# jesli bool == True, to scinamy, w p.p. nie scinamy

# f(i, True) = f(i - 1, False) + C[i]
# f(i, False) = f(i - 1, True)

# f(0, False) = 0
# f(0, True) = C[0]

# poniewaz patrzymy tylko na poprzednia komorke, mozemy zastapic tablice zmiennymi
def czarny_las(C):
  n = len(C)
  dp = [[0, 0] for _ in range(n+1)]

  for i in range(1, n+1):
      dp[i][1] = dp[i-1][0]+C[i-1]
      dp[i][0] = max(dp[i-1][1],dp[i-1][0])
  return max(dp[n][0], dp[n][1])

print(czarny_las([1,3,7,5,6,6,2]))
print(czarny_las([10, 1, 1, 10]))