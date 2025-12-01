import random
import os 
import time
p_card=0
d_card=0
d_hand=0
p_hand=0
can_split=False
card_split=False
errore=True
errore_split_1=True
errore_split_2=True
ut_can_play=True

       
def val_asso():
    global p_card,p_hand,d_card,d_hand
    if p_hand<11:
        p_card=11
    else:
        p_card=1
            
def prima_mano():
            global p_hand,can_split
            first_card1=random.randint(1,13)
            first_c2=random.randint(1,13)
            if first_card1>10:
                first_card1=10
            if first_c2>10:
                first_c2=10
            p_hand+=first_card1
            p_hand+=first_c2
            if first_c2==first_card1:
                can_split=True
        
def Mano_player():
            global p_hand,d_hand,errore,card_split,split_1,split_2,errore_split_1,errore_split_2,can_split
            os.system("cls")
            while errore==True:
                if card_split==False:    
                    print(f"Totale della tua mano:{p_hand}")
                    print(f"Totale della mano del banco:{d_hand}")
                    if can_split:
                        print("Hai due carte uguali,puoi splittare")
                    giocata=input("Scegli la giocata:").strip().capitalize()
                    if giocata!="Chiamo" and giocata!="Passo" and giocata!="Carta" and giocata!="Sto" and giocata!="Split":
                        print("Scelta non valida")
                    else:
                        if giocata=="Split":
                            if can_split:
                                global split_1,split_2
                                
                                split_1=p_hand//2
                                split_2=p_hand//2

                                while errore_split_1==True:
                                    giocata_split=input(f"Sceglia la giocata per la prima mano(Hai un {split_1}):").capitalize().strip()
                                    
                                    if giocata_split!="Chiamo" and giocata_split!="Passo" and giocata_split!="Carta" and giocata_split!="Sto":
                                        print("Scelta non valida")
                                    else:
                                        if giocata_split=="Chiamo" or giocata_split=="Carta":
                                            carta_split1=random.randint(1,13)
                                            if carta_split1>10:
                                                carta_split1=10
                                            if carta_split1==1:
                                                if split_1!=1:
                                                    carta_split1=11
                                            split_1+=carta_split1 
                                            print(f"Nella prima mano hai pescato un {carta_split1}")
                                        
                                        if giocata_split=="Passo" or giocata_split=="Sto":
                                            errore_split_1=False    
                                            while errore_split_2==True:
                                                giocata_split2=input(f"Scegli la giocata per la seconda mano(Hai un {split_2}):")
                                                if giocata_split2!="Chiamo" and giocata_split2!="Passo" and giocata_split2!="Carta" and giocata_split2!="Sto":
                                                    print("Scelta non valida")
                                            
                                                    
                                                else:
                                                    if giocata_split2=="Chiamo" or giocata_split2=="Carta":
                                                        carta_split2=random.randint(1,13)
                                                        if carta_split2>10:
                                                            carta_split2=10
                                                        if carta_split2==1:
                                                            if split_2!=1:
                                                                carta_split2=11
                                                        print(f"Nella seconda mano hai pescato un {carta_split2}") 
                                                        split_2+=carta_split2
                                                        print(f"Totale della prima mano:{split_1}")
                                                        print(f"Totale della seconda mano:{split_2}")
                                                        mano_banco()
                                                        split_errore=False
                                                        card_split=True
                                                    elif giocata_split2=="Passo" or giocata_split2=="Sto":
                                                        mano_banco()
                                                        errore_split_2=False
                                                        card_split=True   
                            else:
                                print("Non puoi splittare(Non hai 2 carte con lo stesso valore)")
                        elif giocata=="Carta" or giocata=="Chiamo":
                            Chiamo_player()
                            os.system("cls")    
                        elif giocata=="Passo" or giocata=="Sto":
                            mano_banco()
                            errore=False
                        
                        
                       
                                
def Chiamo_player():
    global p_card,p_hand
    p_card=random.randint(1,13)
    if p_card>10:
        p_card=10
    if p_card==1:
        val_asso()
    print(f"Hai pescato un {p_card}")
    p_hand+=p_card
    if p_hand>21:
        os.system("cls")
        print("Hai sballato,hai perso!")
        rematch()
    else:
        Mano_player()

def rematch():
    global p_card,p_hand,d_card,d_hand,can_split,card_split,errore,errore_split_1,errore_split_2,ut_can_play
    time.sleep(3)
    os.system("cls")
    p_card=0
    d_card=0
    d_hand=0
    p_hand=0
    can_split=False
    card_split=False
    errore=True
    errore_split_1=True
    errore_split_2=True
    ut_can_play=True
    print("Vuoi fare un'altra partita? (Si/No)")
    risposta=input().strip().capitalize()
    if risposta!="Si" and risposta!="No":
        print("Scelta non valida")
        rematch()
    if risposta=="No":
        print("Grazie per aver giocato!")
    elif risposta=="Si":
        main()      
         
         
   
        
def mano_banco():
            global d_hand,d_card,split_1,split_2,p_hand
            while d_hand<17:
                d_card=random.randint(1,13)
                if d_card>10:
                    d_card=10
                if d_card==1:
                    if d_hand<11:
                        d_card=11
                    else:
                        d_card=1
                print(f"Il banco ha pescato un {d_card}")
                d_hand+=d_card
                if d_hand>21:
                    print("Il banco ha sballato,hai vinto!")
                    rematch()
                
               
            print(f"Il totale della mano del banco è:{d_hand}")
            print(f"Il totale della tua mano è:{p_hand}")
                
            if d_hand>p_hand and d_hand<=21:
                        print("Il banco ha vinto!")
                        rematch()
            elif d_hand<p_hand and p_hand<=21:
                            print("Hai vinto!")
                            rematch()
            elif d_hand==p_hand:
                            print("Pareggio!")
                            rematch()
            if card_split:    
                if d_hand<split_1 and split_1<=21:
                            print("Hai vinto la prima mano!")
                            rematch()
                if d_hand<split_2 and split_2<=21:
                                print("Hai vinto la seconda mano!")
                                rematch()
                if d_hand>split_2 and d_hand<=21:
                                print("Il banco ha vinto la seconda mano!")
                                rematch()
                if d_hand>split_1 and d_hand<=21:
                                print("Il banco ha vinto la prima mano!")
                                rematch()
                            
                
                
        
def prima_manob():
            global d_hand
            prima_Cartab=random.randint(1,13)
            if prima_Cartab>10:
                prima_Cartab=10
            d_hand+=prima_Cartab
def main():
    global p_card,p_hand
    os.system("cls")
    print("BLACKJACK")
    prima_mano()
    prima_manob()
    Mano_player()
main()        

