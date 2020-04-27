#!/usr/bin/python
def triangle_BaseUp(pad, size): 
    output = ("\n".join(pad* " " + int(0.5*size+0.5-i)* " " + ((2*i-1) * "*")
              for i in range(1, int(0.5*size+1.5))))   
    return output

def triangle_BaseDown(pad, size):
    output = ("\n".join((pad* " "+ (i-1)* " "+((size+2-2*i) * "*"))
              for i in range(1, int(0.5*size+1.5))))
    return output

def rhombus(pad, size):
    upper = triangle_BaseUp(pad+1, size-1) 
    lower = triangle_BaseDown(pad, size)  
    output = (upper + "\n" + lower) 
    return output 

print(rhombus(2, 17)) 
