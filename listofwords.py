l=[]
s=[]
N=int(input("enter the list of number: "))
for i in range(1,N+1):
    str=input("enter the string: ")
    l.append(str)
    
print("l=",l)
print("moving the letters which start from vowels to other list")

s=[i for i in l if i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o'or i[0]=='u' or i[0]=='A' or i[0]=='E' or i[0]=='I' or i[0]=='O' or i[0]=='U'] 
    
print("s=",s)