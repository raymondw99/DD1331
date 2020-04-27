#!/usr/bin/python

#Uppgift 2
def rectangle(pad, height, width, char):
     for i in range(height):
         print(pad * " " + str(char) * width)

#Uppgift 3
def frame(height, width, thick): 
     output(width, thick)
     for i in range(height - 2*thick): 
          print(thick *  "*" + ((width-2*thick) * " ") + thick * "*")
     output(width, thick)
          
def output(width, thick):
     for i in range(thick):
          print("*" * width)

#Uppgift 4a
def triangle_BaseUp(pad, base): 
     for i in range(1, int(0.5*base+1.5)):
          print(pad* " "+ (i-1)* " "+((-2*i+base+2) * "*"))

#Uppgift 4b
def triangle_BaseDown(pad, base):
     for i in range(1, int(0.5*base+1.5)):
          print(pad* " " + int(0.5*base+0.5-i)* " "+ ((2*i-1) * "*"))
          
#Uppgift 5
def rhombus(pad, base):
     triangle_BaseDown(pad+1, base-2)
     triangle_BaseUp(pad, base) 

#Körning
def main(): 
     rectangle(13, 5, 29, "+")
     print("")
     frame(10, 30, 3)
     print("")
     triangle_BaseUp(2, 9)
     print("")
     triangle_BaseDown(5, 7)
     print("")
     rhombus(4, 7)

main()
