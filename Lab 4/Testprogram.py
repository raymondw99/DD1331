#!/usr/bin/python
# -*- coding: utf-8 -*-
global elem
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghjiklmnopqrstuvwxyzåäö"

#Öppnar fil
def initial():
    file = open("ordlista.txt", "r").read()
    List = file.split()
    return List

#Binärsökning
def binsearch(List, elem):
    lo = 0
    hi = len(List)-1
    counter = 0 
    while lo <= hi:
        mid = (lo+hi)//2
        print(List[mid])
        counter += 1
        if elem < List[mid]:
            hi = mid - 1
        elif elem > List[mid]:
            lo = mid + 1
        else:
            print("Utskrifter: " + str(counter))
            main() 
    print("Ordet finns inte") 

#Körning
def main():
    try:
        elem = str(input("Ditt ord: "))
        if len(elem) == 5:
            for letter in elem:
                if letter in alphabet:
                    binsearch(initial(), elem)
                    main()
                else:
                    print("Felaktig inmating")
                    main()
        else:
            print("Ogiltig ordlängd")
            main() 
    except:
        return

#Utskrift 
if __name__ == "__main__":
    main()

