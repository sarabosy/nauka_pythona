samolot = {'nazwa':'boeing','przebieg':10000, 'typ':'pasazerski'}

print(samolot.get('cos_innego'))
print(samolot['przebieg'])

for key in samolot:
    print("{0}:{1}".format(key,samolot[key]))

for key, value in samolot.items():
    print("{0}:{1}".format(key,value))
