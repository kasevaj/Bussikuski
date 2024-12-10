import sys
import pygame


def nayta_kortit(korttipakka):
    pygame.init()
    # Luo ikkuna
    naytto = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Korttipeli")
    

    # Lataa korttikuvat
    korttikuvat = {}
    for kortti in korttipakka:
        tiedostonimi = f"korttikuvat/{kortti[0]}_{kortti[1]}.png"  # esim. "pata_5.png"
        korttikuvat[kortti] = pygame.image.load(tiedostonimi)

    # Korttien sijainti ruudulla
    x, y = 50, 50
    askeleet = 110  # Väli korttien välillä

    # Piirrä kortit näytölle
    while True:
        naytto.fill((34, 139, 34))  # Taustaväri (vihreä pöytä)
        
        for i, kortti in enumerate(korttipakka):
            naytto.blit(korttikuvat[kortti], (x + i * askeleet, y))  # Piirrä kortti

        # Päivitä näyttö
        pygame.display.flip()

        # Poistu, jos suljetaan ikkuna
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                sys.exit()