a=int(input("Enter your age: "))

if(a<0):
    print("Invalid Age")
elif(a>=0 and a<=12):
    print("Children Category")
elif(a>=13 and a<=19):
    print("Teenager Category")
elif(a>=20 and a<=59):
    print("Adult Category")
elif(a>=60):
    print("Senior Category")

    
