#!/usr/bin/python
def main():
    try:
        a = int(input("Input number: "))
        b = int(input("Input number: "))
        CubeSum = a**3 + b**3
        print("The Cube sum is equal to " + str(CubeSum))
        main()
    except:
        raise SystemExit 

def message():
    print("Press any non-number key to terminate")

message() 
main()


