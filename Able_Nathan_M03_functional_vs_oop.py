"""
Nathan Able
OOP Calculator vs calculation functions
"""

#Class containing the 4 basic math functions 
class myCalc:
    def __init__(self, val1, val2) -> None:
        self.val1 = val1
        self.val2 = val2

    def add(self):
        return self.val1 + self.val2
    
    def subtract(self):
        return self.val1 - self.val2

    def multiply(self):
        return self.val1 * self.val2

    def divide(self):
        return self.val1 / self.val2

#four basic math functions as independent functions
def addNum(val1, val2):
    return val1 + val2

def subtractNum(val1, val2):
    return val1 - val2

def multiplyNum(val1, val2):
    return val1 * val2

def divideNum(val1, val2):
    return val1 / val2

#My independent object of the myCalc class
myNumbers = myCalc(5,10)

#Values as independent variables
num1 = 5
num2 = 10

#Use class functions to get results of basic math functions
print(myNumbers.add())
print(myNumbers.subtract())
print(myNumbers.multiply())
print(myNumbers.divide())

#Use independent functions to get same results
print(addNum(num1, num2))
print(subtractNum(num1, num2))
print(multiplyNum(num1, num2))
print(divideNum(num1, num2))

#Noted difference. I can create a new object with different numbers without changing the initial object
#with the independent function I would have to define new variables or revalue the curent ones to use the functions



