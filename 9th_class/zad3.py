# mamy formuly logiczne
# zmienne logiczne 0-1 i funkcje logiczne (AND, OR...)
# wyrazenia te sa w postaci CNF:
# AND: "^"; OR: "v";
# np (p OR q OR ~z) AND (~q OR r OR w)

# kazda zmienna moze wystapic w formule maksymalnie 2 razy
# czy da sie tak ustawic wartosciowanie zmiennych aby formula byla spelniona?

# jesli jakas zmienna wystepuje tylko raz, to ustawiam wartosc tej zmiennej tak aby miala wyjsciowo wartosc 1
# np. jesli wystepuje p, to ustawiam p = 1, jest wystepuje ~p, to ustawiam p = 0

# jesli zmienna wystepuje dwa razy i za kazdym razem w tej samej formie (p oraz p lub ~p oraz ~p) to postepujemy j.w.

# w ten sposob mamy formule w ktorej kazda zmienna wystepuje dokladnie dwa razy w roznych formach (p oraz ~p),
# poniewaz jesli byloby inaczej to mozna upraszczac bardziej

# w takiej sytuacji kazda klauzula moze byc spelniona przez jedna zmienna,
# a kazda zmienna moze spelnic dokladnie jedna klauzule


# p1
#           c1
# p2
#           c2
# ...
# p_n        c_m
# jest to graf dwudzielny

# szukamy maksymalnego skojarzenia powyzszzego grafu dwudzielnego,
# poniewaz jedna zmienna satysfakcjonuje maksymalnie jedna klauzule

# skojarzenie - zbior wierzcholkow gdzie zadna krawedz nie jest sasiednia z innymi krawedziami skojarzenia

# tworzymy super zrodlo ktore jest polaczone ze wszystkimi zmiennymi
# oraz super ujscie polaczone ze wszystkiemi klauzulami
# ustawiamy wszystkie wagi na 1

# puszczamy przeplyw, jesli wartosc przeplywu maksymalnego wynosi m, to formula jest spelnialna