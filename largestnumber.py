a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if(a is b and b is c):
    print("All values are same")
elif(a is b):
    print("A and B value are same")
elif(b is c):
    print("B and C value are same")
elif(c is a):
    print("C and A value are same")
elif(a>b):
    if(a>c):
        print(a,"is Max")
    else:
        print(c,"is Max")
else:
    if(b>c):
        print(b ,"is Max")
    else:
        print( c,"is Max")
