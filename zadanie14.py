produkty = {'S1222':'sukienka trojkat','P1222':'spodnie krata','X2X':'konsola do gier'}

igla = 'X2X'
if igla in produkty:
    print("Znalazlam {0}".format(igla))
else:
    print("Brak w magazynie {0}".format(igla))
