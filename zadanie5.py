jezyki = ['python', 'javascript','c++']
print(jezyki[0])
print(jezyki[1])
print(jezyki[2])

for s in jezyki:
    print(s)

for idx in range(len(jezyki)):
    print("idx: "+str(idx)+" : "+jezyki[idx])

print(",".join(jezyki))

arr = "a,b,c,d".split(',')
print(arr)
del arr[1]
arr[1]='f'
print(arr)
