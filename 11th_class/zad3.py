# dwuwymiarowy problem plecakowy
# P = {p_1...p_n}
# p_i = (v_i, w_i, h_i)
# v - wartosc przedmiotu, w - waga przedmiotu, h - wysokosc przedmiotu

# ponadto mamy zadane W - maksymalna waga przedmiotow oraz H - maksymalna wysokosc przedmiotow
# jaka wartosc mozna ukrasc

# tworzymy dwuwymiarowa tablice
# kolumny to rosnace W, wiersze to rosnace H

# T_i(x, y) - maksymalna wartosc skradzionych przedmiotow od 1 do i
# wazacych x i zajmujacych wysokosc y

# T(i, x, y) = max(T(i - 1, x - w_i, y - h_i) + v_i, T(i - 1, x, y))

def knapsack(T, w, h):
  n = len(T)
  dp = [[-float('inf')] * (w + 1) for _ in range(h + 1)]
  dp[0][0] = 0

  #T[w][h][c]
  for k in range(n):
    for i in range(h, -1, -1):
      for j in range(w, -1, -1):
        if dp[i][j] > -float('inf') and i + T[k][1] < h + 1 and j + T[k][0] < w + 1:
          dp[i + T[k][1]][j + T[k][0]] = max(dp[i + T[k][1]][j + T[k][0]], dp[i][j] + T[k][2])

  cost = -float('inf')
  for i in range(h + 1):
    for j in range(w + 1):
      if dp[i][j] > cost:
        cost = dp[i][j]

  return cost
