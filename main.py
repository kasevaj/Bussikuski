import random;

import pygame;
import sys;

from Komponentit.UI import nayta_kortit;
from Komponentit.korttipakka import jaaKortit, luoKorttipakka;

def main():
    print("Luo pakka")
    korttipakka = luoKorttipakka()
    print("Pakka luotu")
    
    maara = int(input("Anna jaettavien korttien määrä: "))
    jaetut_kortit = jaaKortit(maara, korttipakka)
    print("Kortit jaettu:", jaetut_kortit)
    nayta_kortit(korttipakka)

    
if __name__ == "__main__":
    main()


#lajittelufunktiot, lisäyslajittelu, limityslajittelu, kekolajittelu