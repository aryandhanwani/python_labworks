a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))

print("Press 1 for +")
print("Press 2 for -")
print("Press 3 for *")
print("Press 4 for /")
    
choose=int(input("Enter your choise"))

if(choose<=0):
    print("Invalid Choise")
elif(choose==1):
    print(a+b)
elif(choose==2):
    print(a-b)
elif(choose==3):
    print(a*b)
elif(choose==4):
    print(a/b)
    
    
