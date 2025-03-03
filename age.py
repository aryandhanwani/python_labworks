class age():
    
    def __init__(self):
        self.age = 0
        a=int(input("Enter the Age: "))

        if a<self.age:
            print("Age should be greater than 0")
        else:
            self.age=a
    
    def getage(self):
        print(f"Age is {self.age}")

age1=age()
age1.getage()