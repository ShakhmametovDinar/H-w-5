def calc(a, b):
    if b == 0:
        return a
    return calc(a*a, b - 1) 

a = int(input())
b = int(input())
print(calc(a, b-1))