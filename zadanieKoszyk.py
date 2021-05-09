koszyk = {'chleb':3.2, 'maslo': 6.4, 'czekolada':5, 'kawa':16}

najmniejsza =list(koszyk.values())[0]
def licz_ceny(rabat):
    for key in koszyk:
        koszyk[key]=round(koszyk[key]*rabat,2)

def wartosc_koszyka():
    sum=0
    for key in koszyk:
        sum = sum+koszyk[key]
    return sum

if len(koszyk)>5:
    licz_ceny(0.95)
elif wartosc_koszyka() >500:
    licz_ceny(0.9)
elif "mleko" in koszyk:
    # "chleb" or
    temp_key = list(koszyk.keys())[0]
    for key in koszyk:
        if najmniejsza > koszyk[key]:
            najmniejsza = koszyk[key]
            temp_key = key
    koszyk[temp_key]=0
else:
    for i in range(len(koszyk)):
        if (i+1)/3 == 1:
            koszyk[list(koszyk.keys())[i]]=0

print(koszyk)
