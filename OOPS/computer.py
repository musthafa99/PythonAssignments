class Computer:
    def __init__(self,ram,rom,speed):
        self.ram=ram
        self.rom = rom
        self.speed = speed

    def config(self):
        print("RAM is",self.ram,"GB")
        print("ROM is",self.rom, "GB")
        print("Speed is",self.speed, "TB")

ram=int(input())
rom=int(input())
speed=int(input())
computer=Computer(ram,rom,speed)
computer.config()