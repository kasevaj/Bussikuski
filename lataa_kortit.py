import requests
import os

kortti_maa = {
    "S": "pata",
    "H": "hertta",
    "D": "ruutu",
    "C": "risti"
}
kortti_arvot = {
    "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
    "8": "8", "9": "9", "10": "10", "J": "J", "Q": "Q", "K": "K", "A": "A"
}

# Luo korttikuvat-hakemisto, jos sitä ei ole:
os.makedirs("korttikuvat", exist_ok=True)

for maa_koodi, maa_nimi in kortti_maa.items():
    for arvo_koodi, arvo_nimi in kortti_arvot.items():
        arvo_koodi = arvo_koodi if arvo_koodi != "10" else "0"
        url = f"https://deckofcardsapi.com/static/img/{arvo_koodi}{maa_koodi}.png"
        tiedostonimi = f"korttikuvat/{maa_nimi}_{arvo_nimi}.png"
        
        # Lataa ja tallenna kuva:
        response = requests.get(url)
        if response.status_code == 200:
            with open(tiedostonimi, "wb") as f:
                f.write(response.content)
            print(f"Ladattu {tiedostonimi}")
        else:
            print(f"Virhe ladattaessa {url}")