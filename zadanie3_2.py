def calculate(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '/':
        if b !=0:
            return a/b
        else:
            print('Nie mozna dzielic przez 0!')
    elif op == '*':
        return a*b
    return 0

if __name__ == '__main__':
    c = calculate(1,2,'*')
    print(c)
    d = calculate(10,200, '/')
    print(d)
