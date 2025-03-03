class student():
    def __init__(self):
        self.__name__=input("Enter the Name: ")
        self.__roll__=int(input("Enter the Roll Number: "))
        self.__engmarks__=int(input("Enter the Marks obtain in English out of 100: "))
        self.__scimarks__=int(input("Enter the Marks obtain in Science out of 100: "))
        self.__mathmarks__=int(input("Enter the Marks obtain in Maths out of 100: "))

        if self.__engmarks__ >=100:
            print("Invalid marks in English")
        elif self.__scimarks__ >=100:
            print("Invalid marks in Science")
        elif self.__mathmarks__ >=100:
            print("Invalid marks in Maths")

    def avg(self):
        self.__a__=self.__engmarks__+self.__mathmarks__+self.__scimarks__
        self.__avg__=self.__a__/3
        print(f"Average is: {self.__avg__}")
    
    def grade(self):
        if self.__avg__ >= 90:
            print("Grade: A")
        elif self.__avg__>=80:
            print("Grade: B")
        elif self.__avg__>=70:
            print("Grade: C")
        elif self.__avg__>=60 or self.__avg__<60:
            print("Fail")

stu1=student()
stu1.avg()
stu1.grade()

stu2=student()
stu2.avg()
stu2.grade()

stu3=student()
stu3.avg()
stu3.grade()
