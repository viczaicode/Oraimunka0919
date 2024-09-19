import metodusok

#####################################
# BEKÉRÉS // MINDEN FELADATHOZ KELL #
#####################################
bekerendoszam = metodusok.szambekeres()

#####################################
#         // 1. FELADAT //          #
#####################################

pozitivE = metodusok.pozitivE(bekerendoszam)

#####################################
#         // 2. FELADAT //          #
#####################################

egyjegyuEszam = metodusok.egyjegyuE(bekerendoszam)
kisebbszomszed, nagyobbszomszed = metodusok.szomszedszamok(egyjegyuEszam)

#####################################
#         // 3. FELADAT //          #
#####################################

szazalekososztalyzat = metodusok.szazalekososztalyzat(bekerendoszam)

#####################################
#         // 4. FELADAT //          #
#####################################

egeszszamosztalyzat = metodusok.egeszszamososztalyzat(bekerendoszam)

#####################################
#      // GLOBÁLIS KIÍRÁS //        #
#      MINDIG AZ ALJÁN LEGYEN       #
#####################################

metodusok.globaliskiiras(pozitivE, egyjegyuEszam, kisebbszomszed, nagyobbszomszed, szazalekososztalyzat, egeszszamosztalyzat)