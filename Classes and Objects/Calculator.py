class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        result=self.num1+self.num2
        return result

    def sub(self):
        result = self.num1 - self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result

    def divison(self):
        result = self.num1 // self.num2
        return result


calculator=Calculator(56,23)
print("Added Values:",calculator.add())

print("Subtracted Values:",calculator.sub())

print("Multiplied Values:",calculator.multiply())

print("Divided Values:",calculator.divison())