koszyk = {'chleb':3.2,'mleko':10, 'czekolada':2, 'kawa':16}
cena_koszyka =0

for key in koszyk:
    cena_koszyka = cena_koszyka + koszyk[key]

if "chleb" or "mleko" in koszyk:
    cena_koszyka= cena_koszyka*0.9
    
print(cena_koszyka)
