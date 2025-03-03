class book():
    def __init__(self):
        self.__title__= "Build don't talk"
        self.__author__ = "Raj Shamani"

    def getdata(self):
        print(f"Book title is: {self.__title__}\nAuthor is: {self.__author__}")

a=book()

a.getdata()

