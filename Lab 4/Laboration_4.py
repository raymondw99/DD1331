#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import*


#Inläsning av ordlistan
def initial():
    file = open("ordlista.txt", "r").read()
    List = file.split()
    return List

#Linjärsökning
def linsearch(List, elem):
    if elem in List:
        return True
    return False

#Binärsökning 
def binsearch(List, elem):
    lo = 0
    hi = len(List)-1
    while lo <= hi:
        mid = (lo+hi)//2 
        if elem < List[mid]:
            hi = mid - 1
        elif elem > List[mid]:
            lo = mid + 1
        else:
            return True
    return False 

#Utskrift av enkel sökning
def singular_search(List, x):
    elem = str(input("Ditt ord: ")).lower()
    func = [linsearch, binsearch]
    if func[x-1](List, elem):
        print(elem + " finns")
    else:
        print(elem + " finns inte")
    main()

#Utskrift av kuperad sökning                          
def pairsearch(List, func, x):
    message = ['Linjär sökning av kuperade ordpar', 'Binär sökning'
               ' av kuperade ordpar', 'Tidtagning för linjär sökning'
               ' av kuperade ordpar', 'Tidtagning för binär sökning'
               ' av kuperade ordpar']
    print(message[x-3])
    t0 = time()
    for elem in List:
        inverted_elem = elem[2:] + elem[:2]
        if func(List, elem) and func(List, inverted_elem):
            if x == 3 or x == 4: 
                print('[' + elem + ', ' + inverted_elem + ']')
    if x == 5 or x == 6:
        dt = time() - t0
        print("Tid i ms:", round(1000*dt,2))    
    main() 

#Körning
def info():
    print("Välj vad du vill göra (1-5):");
    print("1. Sök upp enstaka ord med linjär sökning")
    print("2. Sök upp enstaka ord med binär sökning")
    print("3. Sök upp kuperade ordpar med linjär sökning")
    print("4. Sök upp kuperade ordpar med binär sökning")
    print("5. Tidtagning för linjär sökning av kuperade ordpar")
    print("6. Tidtagning för binär sökning av kuperade ordpar")
    print("7. Avsluta")

#Körning
def main():
    try: 
        x = int(input(""))
        if x < 7:
            if x < 3:
                singular_search(List, x)
            else:
                func = [linsearch, binsearch, linsearch, binsearch]
                pairsearch(List, func[x-3], x)
        elif x == 7:
            return       
        else:
            error()
    except:
        error()

        
#Felhantering
def error():
    print("Felaktig inmatning")
    main()
   
#Utskrift
if __name__ == "__main__":
    info()
    List = initial()
    main()

