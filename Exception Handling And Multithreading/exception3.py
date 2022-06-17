try:
    f=open("hello.txt",'r')
    f.readline()
except Exception as e:
    print(e)

    