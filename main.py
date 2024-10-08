#import metodusok
import gyakorlok

#-----------------------------------------------------------############################################################-----------------------------------------------------------#
#---------------------------------------------------------- #     ELÁGAZÁS FELADATOK // SZEDD KI KOMMENTEKEBŐL         #-----------------------------------------------------------#
#-----------------------------------------------------------#            HA MŰKÖDÉSRE SZERETNÉD BÍRNI                  #-----------------------------------------------------------#
#-----------------------------------------------------------############################################################-----------------------------------------------------------#

#####################################
# BEKÉRÉS // MINDEN FELADATHOZ KELL #
#####################################
#bekerendoszam = metodusok.szambekeres()

#####################################
#         // 1. FELADAT //          #
#####################################

#pozitivE = metodusok.pozitivE(bekerendoszam)

#####################################
#         // 2. FELADAT //          #
#####################################

#egyjegyuEszam = metodusok.egyjegyuE(bekerendoszam)
#kisebbszomszed, nagyobbszomszed = metodusok.szomszedszamok(egyjegyuEszam)

#####################################
#         // 3. FELADAT //          #
#####################################

#szazalekososztalyzat = metodusok.szazalekososztalyzat(bekerendoszam)

#####################################
#         // 4. FELADAT //          #
#####################################

#egeszszamosztalyzat = metodusok.egeszszamososztalyzat(bekerendoszam)

#####################################
#      // GLOBÁLIS KIÍRÁS //        #
#      MINDIG AZ ALJÁN LEGYEN       #
#####################################

#metodusok.globaliskiiras(pozitivE, egyjegyuEszam, kisebbszomszed, nagyobbszomszed, szazalekososztalyzat, egeszszamosztalyzat)


#-----------------------------------------------------------############################################################-----------------------------------------------------------#
#---------------------------------------------------------- #     GYAKORLÓ FELADATOK // SZEDD KI KOMMENTEKEBŐL         #-----------------------------------------------------------#
#-----------------------------------------------------------#            HA MŰKÖDÉSRE SZERETNÉD BÍRNI                  #-----------------------------------------------------------#
#-----------------------------------------------------------############################################################-----------------------------------------------------------#


#####################################
# BEKÉRÉS // MINDEN FELADATHOZ KELL #
#####################################

bekertszam = gyakorlok.szambekeres()

#####################################
#         // 1. FELADAT //          #
#####################################

abszolutszam = gyakorlok.abszolutertek(bekertszam)

#####################################
#         // 17. FELADAT //          #
#####################################

ketjegyuszam, ketjegyuE = gyakorlok.ketjegyuE(bekertszam)

#####################################
#         // 21. FELADAT //          #
#####################################

legkisebb = gyakorlok.legkisebb()

#####################################
#      // GLOBÁLIS KIÍRÁS //        #
#      MINDIG AZ ALJÁN LEGYEN       #
#####################################

gyakorlok.globalisprintgyakorlo(abszolutszam, ketjegyuszam, ketjegyuE, legkisebb)



