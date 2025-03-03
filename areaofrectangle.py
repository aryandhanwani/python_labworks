class rectangle():
    def __init__(self):
        self.width=int(input("enter the width: "))
        self.length=int(input("enter the length "))
    
    def getdata(self):

        self.area=self.width*self.length
        
        print(f"area of rectangle is : {self.area}")

a=rectangle()

a.getdata()
