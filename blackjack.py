import pygame
from random import randint

pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Menu")
#Formattazione Immagini 

# Colori
VERDE = (0, 150, 0)
BIANCO = (255, 255, 255)
GRIGIO = (180, 180, 180)
GRIGIO_SCURO = (100, 100, 100)
NERO = (0, 0, 0)
GIALLO = (255, 222, 0)

font_titolo = pygame.font.SysFont(None, 72)
font_bottone = pygame.font.SysFont(None, 48)


carte_asset={
    "2":pygame.transform.scale(pygame.image.load("assets/carte/2.png"), (120, 150)),
    "3":pygame.transform.scale(pygame.image.load("assets/carte/3.png"), (120, 150)),
    "4":pygame.transform.scale(pygame.image.load("assets/carte/4.png"), (120, 150)),
    "5":pygame.transform.scale(pygame.image.load("assets/carte/5.png"), (120, 150)),
    "6":pygame.transform.scale(pygame.image.load("assets/carte/6.png"), (120, 150)),
    "7":pygame.transform.scale(pygame.image.load("assets/carte/7.png"), (120, 150)),
    "8":pygame.transform.scale(pygame.image.load("assets/carte/8.png"), (120, 150)),
    "9":pygame.transform.scale(pygame.image.load("assets/carte/9.png"), (120, 150)),
    "10":pygame.transform.scale(pygame.image.load("assets/carte/10.png"), (120, 150)),
    "J":pygame.transform.scale(pygame.image.load("assets/carte/J.png"), (120, 150)),
    "Q":pygame.transform.scale(pygame.image.load("assets/carte/Q.png"), (120, 150)),
    "K":pygame.transform.scale(pygame.image.load("assets/carte/K.png"), (120, 150)),
    "A":pygame.transform.scale(pygame.image.load("assets/carte/A.png"), (120, 150)),
}

rett_pulsanti={
    "play":pygame.Rect(WIDTH//2 - 120, 180, 240, 60),           "play hover":pygame.Rect(WIDTH//2 - 120, 180, 240, 60),
    "exit":pygame.Rect(WIDTH//2 - 120, 270, 240, 60),           "exit hover":pygame.Rect(WIDTH//2 - 120, 270, 240, 60),
    "call":pygame.Rect(WIDTH//2 - 260, 500, 120, 50),           "call hover":pygame.Rect(WIDTH//2 - 260, 320, 120, 50),
    "step":pygame.Rect(WIDTH//2 + 140, 500, 120, 50),           "step hover":pygame.Rect(WIDTH//2 + 140, 320, 120, 50),
    "split":pygame.Rect(WIDTH//2 - 60, 500, 120, 50),           "split hover":pygame.Rect(WIDTH//2 - 60, 320, 120, 50),
    "fiche":pygame.Rect(WIDTH - 150, 20, 130, 50),              "fiche hover":pygame.Rect(WIDTH - 150, 20, 130, 50),
    "exit game":pygame.Rect(WIDTH - 70, HEIGHT - 70, 50, 50),   "exit game hover":pygame.Rect(WIDTH - 70, HEIGHT - 70, 50, 50),

}



def main():
    first_hand()
    global first_card, second_card
    while True:
       
        WIN.fill(VERDE)
        
        draw_card(carte_asset[first_card], 50, 100)
        draw_card(carte_asset[second_card], 200, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if rett_pulsanti["call"].collidepoint(mx, my):
                    print("Chiamata")
                if rett_pulsanti["step"].collidepoint(mx, my):
                    print("Passo")
                if rett_pulsanti["fiche"].collidepoint(mx, my):
                    print("Aggiungi Fiche")
                

        pygame.display.update()
    
def first_hand():
    first_card_val=randint(1,13)
    second_card_val=randint(1,13)
    if first_card_val==11:
        first_card="J"
        first_card_val=10
    elif first_card_val==12:
        first_card="Q"
        first_card_val=10
    elif first_card_val==13:
        first_card="K"
        first_card_val=10
    elif first_card_val==1:
        first_card="A"
        #val_asso(first_card_val)
    else:
        first_card=str(first_card)
    if second_card_val==11:
        second_card="J"
        second_card_val=10
    elif second_card_val==12:
        second_card="Q"
        second_card_val=10
    elif second_card_val==13:
        second_card="K"
        second_card_val=10
    elif second_card_val==1:
        second_card="A"
        #val_asso(second_card_val)
    else:
        second_card=str(second_card)
    p_hand=first_card_val+second_card_val
    if p_hand==21:
        WIN.fill(VERDE)
        blackjack_p = font_titolo.render("BLACKJACK", True, GIALLO) 
        WIN.blit(blackjack_p, (WIDTH//2 - blackjack_p.get_width()//2, 60))
        pygame.display.update()               
    return first_card, second_card, p_hand
    
    
 
def draw_menu():
    WIN.fill(VERDE)
    # Titolo
    testo = font_titolo.render("Blackjack", True, GIALLO) 
    WIN.blit(testo, (WIDTH//2 - testo.get_width()//2, 60))

    # Pulsanti
    btn_start = rett_pulsanti["play"]
    btn_exit = rett_pulsanti["exit"]

    pygame.draw.rect(WIN, GRIGIO, btn_start)
    pygame.draw.rect(WIN, GRIGIO, btn_exit)

    start_txt = font_bottone.render("Inizia", True, NERO)
    exit_txt = font_bottone.render("Esci", True, NERO)
    WIN.blit(start_txt, (btn_start.x + btn_start.width//2 - start_txt.get_width()//2,
                         btn_start.y + btn_start.height//2 - start_txt.get_height()//2))
    WIN.blit(exit_txt, (btn_exit.x + btn_exit.width//2 - exit_txt.get_width()//2,
                        btn_exit.y + btn_exit.height//2 - exit_txt.get_height()//2))
    return btn_start, btn_exit

def menu_loop():
    while True:
        btn_start, btn_exit = draw_menu()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if btn_start.collidepoint(mx, my):
                    main()
                if btn_exit.collidepoint(mx, my):
                    pygame.quit()
                    
def draw_card(card, x, y):
    card=randint(1,13)
    if card==11:
        card="J"
    elif card==12:
        card="Q"
    elif card==13:
        card="K"
    elif card==1:
        card="A"
    else:
        card=str(card)
    WIN.blit(carte_asset[card], (x, y))
    x+=carte_asset[card].get_width()+10
    return x

if __name__ == "__main__":
    menu_loop()


while True:
    menu_loop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            pygame.quit()
         

