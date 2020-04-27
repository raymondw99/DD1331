#!/usr/bin/python
# -*- coding: utf-8 -*-
List = []

#Skapar kortlek
def create_card(var):
    card = []
    for i in range(var):
        card.append(i);
    return card

#Körning
def main():
    try: 
        var = int(input("Kortstorlek: "))
        if len(create_card(var)) % 2 != 0: 
            print("Felaktig inmatning")
            var = 0
            main()
        else:
            output(create_card(var), var, List)
            main()
    except:
        print("För stort värde")
        var = 0
        main()
        
#Huvudalgoritm med rekusiv definition
def output(x, var, List):
    half_point = int(len(x)/2)
    a = x[:half_point]
    b = x[half_point:]
    m = (riffle(a, b))
    List.append(m)
    if m != create_card(var):
        output(m, var, List)
    else:
        print(str(len(List)) + " gånger")
        List.clear()
        var = 0
        return
    
#Riffelblandar    
def riffle(deck1, deck2):
    if not deck1:
        return deck2
    elif not deck2:
        return deck1
    return deck1[0:1] + riffle(deck2, deck1[1:])

#Informationstext
def info():
    print("Hur många riffelblandningar för att få")
    print("den ursprungliga ordningen?")

#Utskrift 
if __name__ == "__main__":
    info()
    main()

