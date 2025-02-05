class Class:
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())

x = Class()
x.getString()
x.printString()