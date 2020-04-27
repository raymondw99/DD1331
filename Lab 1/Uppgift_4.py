#!/usr/bin/python
def message():
    print("          Determine Ramanujan integers         ")   
    print("        Calculate (a,b) to a^3 + b^3 = N       ")
    print("Not a Ramanujan number if no integers are found")
    print("") 

def main():
    try: 
        num = int(input("Input N: "))
        for a in range(1,(round(num**3) +1)):
            try:
                b = (num - a**3)**(1/3)
                n = (a**3 + (round(b)**3))
                if n == num:
                    if a <= b:
                        print(str(a) + ", " + str(round(b)))
            except TypeError:
                break
    except:
        print("Type in integers, please try again")
        main() 
        
message()    
main()
