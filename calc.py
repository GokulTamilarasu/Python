def add(n1,n2):
    return f'{n1} + {n2} = {n1+n2}'
def subtract(n1,n2):
    return f'{n1} - {n2} = {n1-n2}'
def multiply(n1,n2):
    return f'{n1} * {n2} = {n1*n2}'
def divide(n1,n2):
    return f'{n1} / {n2} = {n1/n2}'

operations={'+':add,'-':subtract,'*':multiply,'/':divide}

n1=float(input("what is the first number? "))
for symbol in operations:
    print(symbol)
operator=input("pick an operator : ")
n2=float(input("what is the second number? "))
print(operations[operator](n1, n2))
new_or_not=input("")