import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Menu")

# Colori
VERDE = (0, 150, 0)
BIANCO = (255, 255, 255)
GRIGIO = (180, 180, 180)
NERO = (0, 0, 0)
GIALLO = (255, 222, 0)

font_titolo = pygame.font.SysFont(None, 72)
font_bottone = pygame.font.SysFont(None, 48)


carte_asset={
    


}

rett_pulsanti={}

rett_carte

def() draw_table

def main():

def draw_menu():
    WIN.fill(VERDE)
    # Titolo
    testo = font_titolo.render("Blackjack", True, GIALLO) 
    WIN.blit(testo, (WIDTH//2 - testo.get_width()//2, 60))

    # Pulsanti
    btn_start = pygame.Rect(WIDTH//2 - 120, 180, 240, 60)
    btn_exit = pygame.Rect(WIDTH//2 - 120, 270, 240, 60)

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
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if btn_start.collidepoint(mx, my):
                    main()
                if btn_exit.collidepoint(mx, my):
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    menu_loop()
