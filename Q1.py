def num(n):
    if n==1:
        return 0
    else:
        return n+(num(n-1))
n=int(input("enter : "))
print(num)