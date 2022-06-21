class Bank:
    def getroi(self):
        return 8;

class SBI(Bank):
    def getroi(self):
        return 9;

class Axis(Bank):
    def getroi(self):
        return 10;

b1=Bank()
b2=SBI()
b3=Axis()

print("Bank Rate of Interest:",b1.getroi())
print("SBI Bank Rate of Interest:",b2.getroi())
print("AXIS Bank Rate of Interest:",b3.getroi())