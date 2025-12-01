import pygame
from random import randint

pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Blackjack Menu")
#Formattazione Immagini 

# Colori
VERDE = (0, 150, 0)
BIANCO = (255, 255, 255)
GRIGIO = (180, 180, 180)
GRIGIO_SCURO = (100, 100, 100)
NERO = (0, 0, 0)
GIALLO = (255, 222, 0)
#Testi
font_titolo = pygame.font.SysFont(None, 72)
font_bottone = pygame.font.SysFont(None, 48)
#Variabili di gioco
first_turn=True
can_split=False
card_split=False
pc_turn=False
blacjack_pc=True
tot=0
player_cards=[]
busted=False
dealer_cards=[]
dealer_tot=0
dealer_busted=False
dealer_hidden=True
game_over=False
winner=None



carte_asset={
    "2":pygame.transform.scale(pygame.image.load("assets/carte/2.png"), (90, 112)),
    "3":pygame.transform.scale(pygame.image.load("assets/carte/3.png"), (90, 112)),
    "4":pygame.transform.scale(pygame.image.load("assets/carte/4.png"), (90, 112)),
    "5":pygame.transform.scale(pygame.image.load("assets/carte/5.png"), (90, 112)),
    "6":pygame.transform.scale(pygame.image.load("assets/carte/6.png"), (90, 112)),
    "7":pygame.transform.scale(pygame.image.load("assets/carte/7.png"), (90, 112)),
    "8":pygame.transform.scale(pygame.image.load("assets/carte/8.png"), (90, 112)),
    "9":pygame.transform.scale(pygame.image.load("assets/carte/9.png"), (90, 112)),
    "10":pygame.transform.scale(pygame.image.load("assets/carte/10.png"), (90, 112)),
    "J":pygame.transform.scale(pygame.image.load("assets/carte/J.png"), (90, 112)),
    "Q":pygame.transform.scale(pygame.image.load("assets/carte/Q.png"), (90, 112)),
    "K":pygame.transform.scale(pygame.image.load("assets/carte/K.png"), (90, 112)),
    "A":pygame.transform.scale(pygame.image.load("assets/carte/A.png"), (90, 112)),
}

rett_pulsanti={
    "play":pygame.Rect(WIDTH//2 - 120, 180, 240, 60),           "play hover":pygame.Rect(WIDTH//2 - 120, 180, 240, 60),
    "exit":pygame.Rect(WIDTH//2 - 120, 270, 240, 60),           "exit hover":pygame.Rect(WIDTH//2 - 120, 270, 240, 60),
    "call":pygame.Rect(WIDTH//2 + 100, 500, 120, 50),           "call hover":pygame.Rect(WIDTH//2 - 260, 320, 120, 50),
    "step":pygame.Rect(WIDTH//2 + 250, 500, 120, 50),           "step hover":pygame.Rect(WIDTH//2 + 140, 320, 120, 50),
    "split":pygame.Rect(800, 500, 120, 50),                     "split hover":pygame.Rect(WIDTH//2 - 60, 320, 120, 50),
    "fiche":pygame.Rect(WIDTH - 150, 20, 130, 50),              "fiche hover":pygame.Rect(WIDTH - 150, 20, 130, 50),
    "exit game":pygame.Rect(WIDTH - 70, HEIGHT - 70, 50, 50),   "exit game hover":pygame.Rect(WIDTH - 70, HEIGHT - 70, 50, 50),

}



def main():
    global tot, player_cards, busted, dealer_cards, dealer_tot, dealer_hidden, game_over, winner
    tot=0
    player_cards=[]
    busted=False
    dealer_cards=[]
    dealer_tot=0
    dealer_hidden=True
    game_over=False
    winner=None
    card_pesca()  # Draw initial two cards for player
    dealer_draw()  # Draw initial two cards for dealer
    while True:
        WIN.fill(VERDE)
        dealer_card_draw()
        card_draw()
        pygame.draw.rect(WIN, GRIGIO, rett_pulsanti["call"])
        text_call = font_bottone.render("Call", True, NERO)
        WIN.blit(text_call, (rett_pulsanti["call"].x + (rett_pulsanti["call"].width - text_call.get_width()) // 2,rett_pulsanti["call"].y + (rett_pulsanti["call"].height - text_call.get_height()) // 2))
        pygame.draw.rect(WIN, GRIGIO, rett_pulsanti["step"])
        text_step = font_bottone.render("Step", True, NERO)
        WIN.blit(text_step, (rett_pulsanti["step"].x + (rett_pulsanti["step"].width - text_step.get_width()) // 2,rett_pulsanti["step"].y + (rett_pulsanti["step"].height - text_step.get_height()) // 2))
        text_totale = font_bottone.render(f"Totale:{tot} ", True, BIANCO)
        WIN.blit(text_totale, ((WIDTH//2 - text_totale.get_width()//2)+250, 400))
        if busted:
            text_sforato = font_bottone.render("Hai sforato!", True, BIANCO)
            WIN.blit(text_sforato, (WIDTH//2 - text_sforato.get_width()//2, 100))
        if game_over:
            if winner == "player":
                text_win = font_bottone.render("Hai vinto!", True, BIANCO)
            elif winner == "dealer":
                text_win = font_bottone.render("Hai perso!", True, BIANCO)
            else:
                text_win = font_bottone.render("Pareggio!", True, BIANCO)
            WIN.blit(text_win, (WIDTH//2 - text_win.get_width()//2, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if rett_pulsanti["call"].collidepoint(mx, my):
                    card_pesca()
                if rett_pulsanti["step"].collidepoint(mx, my):
                    dealer_turn()
                if rett_pulsanti["fiche"].collidepoint(mx, my):
                    print("Aggiungi Fiche")


        pygame.display.update()
    
def start_menu():
    while True:
        WIN.fill(VERDE)
        texct_titolo = font_titolo.render("Blackjack", True, GIALLO)
        WIN.blit(texct_titolo, (WIDTH//2 - texct_titolo.get_width()//2, 80))
        
        pygame.draw.rect(WIN, GRIGIO, rett_pulsanti["play"])
        text_play = font_bottone.render("Play", True, NERO)
        WIN.blit(text_play, (rett_pulsanti["play"].x + (rett_pulsanti["play"].width - text_play.get_width()) // 2,rett_pulsanti["play"].y + (rett_pulsanti["play"].height - text_play.get_height()) // 2))
        pygame.draw.rect(WIN, GRIGIO, rett_pulsanti["exit"])
        text_exit = font_bottone.render("Exit", True, NERO)
        WIN.blit(text_exit, (rett_pulsanti["exit"].x + (rett_pulsanti["exit"].width - text_exit.get_width()) // 2,rett_pulsanti["exit"].y + (rett_pulsanti["exit"].height - text_exit.get_height()) // 2))
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if rett_pulsanti["play"].collidepoint(mx, my):
                    main()
                if rett_pulsanti["exit"].collidepoint(mx, my):
                    pygame.quit()

        pygame.display.update()
def card_draw():
    global player_cards
    for i, card in enumerate(player_cards):
        WIN.blit(carte_asset[card], (WIDTH//2 - 200 + i * 120, HEIGHT//2 - 75))

def dealer_draw():
    global dealer_cards, dealer_tot
    cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    first_card = cards[randint(0,12)]
    second_card = cards[randint(0,12)]
    dealer_cards.append(first_card)
    dealer_cards.append(second_card)
    dealer_tot = calculate_total(dealer_cards)

def dealer_card_draw():
    global dealer_cards, dealer_hidden
    for i, card in enumerate(dealer_cards):
        if i == 1 and dealer_hidden:
            WIN.blit(pygame.transform.scale(pygame.image.load("assets/back.png"), (90, 112)), (WIDTH//2 - 200 + i * 120, HEIGHT//2 - 200))
        else:
            WIN.blit(carte_asset[card], (WIDTH//2 - 200 + i * 120, HEIGHT//2 - 200))
def card_pesca():
    global tot, first_turn, player_cards, busted
    cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    if first_turn:
        first_card = cards[randint(0,12)]
        second_card = cards[randint(0,12)]
        player_cards.append(first_card)
        player_cards.append(second_card)
        first_turn = False
    else:
        card = cards[randint(0,12)]
        player_cards.append(card)
    tot = calculate_total(player_cards)
    if tot > 21:
        busted = True
    return player_cards[-1] if player_cards else None
def calculate_total(cards):
    total = 0
    aces = 0
    for card in cards:
        if card in ["J","Q","K"]:
            total += 10
        elif card == "A":
            aces += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def dealer_turn():
    global dealer_hidden, dealer_tot, dealer_busted, game_over, winner, busted, tot
    dealer_hidden = False  # Reveal hidden card
    while dealer_tot < 17 and not dealer_busted:
        cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        card = cards[randint(0,12)]
        dealer_cards.append(card)
        dealer_tot = calculate_total(dealer_cards)
        if dealer_tot > 21:
            dealer_busted = True
    # Determine winner
    game_over = True
    if busted:
        winner = "dealer"
    elif dealer_busted:
        winner = "player"
    elif tot > dealer_tot:
        winner = "player"
    elif tot < dealer_tot:
        winner = "dealer"
    else:
        winner = "tie"

def card_value(card):
    if card in ["J","Q","K"]:
        return 10
    elif card == "A":
        return 11  # Default to 11, adjust in calculate_total
    else:
        return int(card)
start_menu()

