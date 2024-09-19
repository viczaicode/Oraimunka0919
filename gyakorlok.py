import math

def szambekeres(): #UGYANÍGY NEVEZTEM EL A BEKÉRŐ FÜGGVÉNYT A METODUSOK.PY-BAN NE KAVARODJ ÖSSZE
    bekertszam:int = int(input("Kérem adjon meg egy számot amivel a továbbiakban tudok dolgozni: "))
    return bekertszam

def abszolutertek(abszolutszam:int):
    abszolutszam = math.fabs(abszolutszam)
    return abszolutszam











def globalisprintgyakorlo(abszolutszam):
    print(f"A beírt számnak az abszolútértéke math.fabs-al számolva: {abszolutszam}")