b=[]
a=int(input("enter number: "))
while (a!=0):
    b.append(a)
    a=int(input("enter number: "))
print(b[::-1])
