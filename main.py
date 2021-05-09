produkty=['chleb', 'maslo', 'czekolada', 'kawa']
ceny=[2.3, 4.5, 2, 16]
najmniejsza =ceny[0]

def licz_ceny(rabat):
    for i in range(len(ceny)):
        ceny[i]=round(ceny[i]*rabat,2)

koszyk=[produkty, ceny]
if len(produkty)>5:
    licz_ceny(0.95)
elif sum(ceny)>500:
    licz_ceny(0.9)
else:
    # for i in ceny:
    #     if najmniejsza > i:
    #         najmniejsza = i
    # ceny[ceny.index(najmniejsza)]=0
    for i in range(len(ceny)):
        if (i+1)/3 == 1:
            ceny[i]=0

print(koszyk)
