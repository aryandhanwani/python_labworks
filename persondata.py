class person:
    __name__=None
    __age__=None

    def setdata(self):
        self.__name__=input("Enter the Name: ")
        self.__age__=int(input("Enter the Age: "))
    
    def getdata(self):
        print(f"Name is : {self.__name__}\nAge is: {self.__age__}")


p1=person()
p2=person()

p1.setdata()
p2.setdata()

print("Person's Data are:- ")

p1.getdata()
p2.getdata()