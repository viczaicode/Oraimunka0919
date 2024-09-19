import math

def szambekeres(): #UGYANÍGY NEVEZTEM EL A BEKÉRŐ FÜGGVÉNYT A METODUSOK.PY-BAN NE KAVARODJ ÖSSZE
    bekertszam:int = int(input("Kérem adjon meg egy számot amivel a továbbiakban tudok dolgozni: "))
    return bekertszam

def abszolutertek(abszolutszam:int):
    abszolutszam = math.fabs(abszolutszam)
    return abszolutszam

#KÖTELEZŐ HÁZI FELADATOK ELŐBB 15.,17.,21

#17

def ketjegyuE(ketjegyuszam:int):
    if (ketjegyuszam >= 10 and ketjegyuszam < 100):
        ketjegyuE = True
        return ketjegyuszam, ketjegyuE
    else:
        ketjegyuE = False
        return ketjegyuszam, ketjegyuE
    




def globalisprintgyakorlo(abszolutszam, ketjegyuszam, ketjegyuE):
    print(f"A beírt számnak az abszolútértéke math.fabs-al számolva: {abszolutszam}")
    if (ketjegyuE):
        print(f"A beírt számot leellenőriztem, és kétjegyű. A szám {ketjegyuszam}")
    else:
        print(f"A beírt számot leellenőriztem, és nem kétjegyű. A szám {ketjegyuszam}")