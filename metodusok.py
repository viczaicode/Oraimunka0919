def szambekeres():
    bekerendoszam:int = int(input("Kérem adjon meg egy számot amivel a továbbiakban tudok dolgozni: "))
    return bekerendoszam

def pozitivE(pozitivEszam:int):
    if (int(pozitivEszam) > 0):
        return "A megadott szám pozitív"
    else:
        return ""
    
def egyjegyuE(egyjegyuEszam:int):
    if (int(egyjegyuEszam) < 10 and int(egyjegyuEszam) > -10):
        return int(egyjegyuEszam)
    else:
        return 0
    
def szomszedszamok(egyjegyuEszam:int):
    nagyobbszomszed:int = egyjegyuEszam + 1
    kisebbszomszed:int = egyjegyuEszam - 1
    return kisebbszomszed, nagyobbszomszed

def szazalekososztalyzat(szazalekoseredmeny):
    if (szazalekoseredmeny >= 0 and szazalekoseredmeny <= 100):
        if (szazalekoseredmeny >= 0 and szazalekoseredmeny < 60):
            return "Elégtelen"
        elif (szazalekoseredmeny >= 60 and szazalekoseredmeny < 70):
            return "Elégséges"
        elif (szazalekoseredmeny >= 70 and szazalekoseredmeny < 80):
            return "Közepes"
        elif (szazalekoseredmeny >= 80 and szazalekoseredmeny < 90):
            return "Jó"
        elif (szazalekoseredmeny >= 90 and szazalekoseredmeny <= 100):
            return "Jeles"
        else:
            return "Hiba: érvénytelen százalék!"
        
def egeszszamososztalyzat(egeszSzamOsztalyzat):
    if (egeszSzamOsztalyzat == 1):
        return egeszSzamOsztalyzat
    elif (egeszSzamOsztalyzat == 2):
        return egeszSzamOsztalyzat
    elif (egeszSzamOsztalyzat == 3):
        return egeszSzamOsztalyzat
    elif (egeszSzamOsztalyzat == 4):
        return egeszSzamOsztalyzat
    elif (egeszSzamOsztalyzat == 5):
        return egeszSzamOsztalyzat
    
def globaliskiiras(pozitivEReturn:str,egyjegyuEszam:int,kisebbszomszed:int, nagyobbszomszed:int, szazalekososztalyzat:int, egeszSzamOsztalyzat:int):
    if not (pozitivEReturn == ""):
        print(pozitivEReturn)
    if (egyjegyuEszam != 0):
        print(f"Mivel a megadott szám egyjegyű volt, ezért kiírom az egyel kisebb, és nagyobb szomszédjait: {kisebbszomszed}, {nagyobbszomszed}")
    print(f"Az elért osztályzat: {szazalekososztalyzat}")

    if (egeszSzamOsztalyzat == 1):
        print(f"Az egész számos osztályzat eredménye: Elégtelen ({egeszSzamOsztalyzat})")
    elif (egeszSzamOsztalyzat == 2):
        print(f"Az egész számos osztályzat eredménye: Elégséges ({egeszSzamOsztalyzat})")
    elif (egeszSzamOsztalyzat == 3):
        print(f"Az egész számos osztályzat eredménye: Közepes ({egeszSzamOsztalyzat})")
    elif (egeszSzamOsztalyzat == 4):
        print(f"Az egész számos osztályzat eredménye: Jó ({egeszSzamOsztalyzat})")
    elif (egeszSzamOsztalyzat == 5):
        print(f"Az egész számos osztályzat eredménye: Jeles ({egeszSzamOsztalyzat})")
