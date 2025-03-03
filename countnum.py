class counter:
    __count=0
    
    def increment(self):
        self.__count+=1

    def display(self):
        print(f"Count is: {self.__count}")
        
c1=counter()

c1.increment()
c1.display()

c1.increment()
c1.increment()

c1.display()