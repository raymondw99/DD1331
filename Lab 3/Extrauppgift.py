from languages import *

def info():
    print("Vilket språk önskas?")
    print("1 Visk 2 Rövar 3 Bebis")
    print("4 All 5 Fikon 6 Avsluta programmet")

def main():
    try:
        selection()
    except ValueError:
        print("Mata in igen")
        selection()
        
def selection():
    choice = int(input("")) - 1
    while choice != 5:
        text = str(input("Din mening: "))
        menu = [whisper_convert(text), robbers_convert(text),
        baby_convert(text), all_convert(text), fig_convert(text)]
        language = ["Viskspråket: ", "Sjörövarspråket: ", "Bebisspråket: ",
                    "Allspråket: ", "Fikonspråket: "]
        print(language[choice] + menu[choice])
        main() 
    print("Programmet avslutas")
    raise SystemExit()

    
info()
main() 
