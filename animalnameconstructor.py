class animal():
    
    def __init__(self):
       self.a1=input("Enter the name of Animal: ")
      
    def getdata(self):
        print(f"Animal Name is: {self.a1}")
        
a=animal()
b=animal()
a.getdata()
b.getdata()