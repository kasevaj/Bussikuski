import random


def luoKorttipakka():
    korttipakka = []
    numerot = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    maat = ("pata", "risti", "ruutu", "hertta")

    for maa in maat:
        for numero in numerot:
            kortti = (maa, numero)
            korttipakka.append(kortti)

    random.shuffle(korttipakka)
    return korttipakka

def jaaKortit(maara, korttipakka):
    listaJaetut = []  # Oikea tietorakenne listalle
    for _ in range(maara):
        if korttipakka:
            jaettu = korttipakka.pop()  # Poistaa viimeisen kortin pakasta
            listaJaetut.append(jaettu)
        else:
            print("Pakka on tyhjä!")
            break
    return listaJaetut