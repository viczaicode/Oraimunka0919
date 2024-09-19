import metodusok

bekerendoszam = metodusok.szambekeres()
pozitivE = metodusok.pozitivE(bekerendoszam)
egyjegyuEszam = metodusok.egyjegyuE(bekerendoszam)
kisebbszomszed, nagyobbszomszed = metodusok.szomszedszamok(egyjegyuEszam)
szazalekososztalyzat = metodusok.szazalekososztalyzat(bekerendoszam)

metodusok.globaliskiiras(pozitivE, egyjegyuEszam, kisebbszomszed, nagyobbszomszed, szazalekososztalyzat)