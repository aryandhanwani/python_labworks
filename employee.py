class employee():

    def __init__(self):
        self.name="Alice"
        self.exp=3
        self.salary=50000

    def display(self):
        print("Name:",self.name)
        print("Experience:",self.exp)
        print("Salary:",self.salary)
    
    def __del__(self):
        print("It was a good Experince with you....")

e1=employee()

e1.display()

del e1