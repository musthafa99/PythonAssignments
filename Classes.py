class Computer:
    def config(self,ram,rom,speed):
        print("RAM is",ram,"GB")
        print("ROM is", rom, "GB")
        print("Speed is", speed, "TB")

ram=int(input())
rom=int(input())
speed=int(input())
computer=Computer()
computer.config(ram,rom,speed)