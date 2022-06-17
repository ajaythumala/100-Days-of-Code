#the blackjack game project

import random 

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0 #0 is the indicator of a blackjack and gives you an instant win
    elif sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(pl_score,pc_score):
    #dealer's cards aren't revealed yet
    #so you lose even if the dealer is over 21 if your score is over 21
    if pl_score > 21 and pc_score > 21:
        return "You went over. You lose :("

    if pl_score == pc_score:
        return "Draw :| "
    elif pc_score == 0:
        return "Lose, opponent has Blackjack :( "
    elif pl_score == 0:
        return "Win with a Blackjack :) "
    elif pl_score > 21:
        return "You went over. You lose :("
    elif pc_score > 21:
        return "Opponent went over. You win :) "
    elif pl_score > pc_score:
        return "You win :) "
    else:
        return "You lose :("

def play_game():
    player=[]
    pc=[]

    for _ in range(2):
        player.append(deal_card())
        pc.append(deal_card())

    end=False
    while(not end):
        player_score=calculate_score(player)
        pc_score=calculate_score(pc)

        print("    Your cards:",player,"score:",player_score)
        print("    Dealer's first card:",pc[0],"score:",pc_score,"--for testing purposes--")

        if player_score == 0 or pc_score == 0 or player_score>21:
            end=True
        else:
            deal=input("Do you want to hit or stay? 'y' or 'n'? ")
            if deal == 'y':
                player.append(deal_card())
            else:
                end=True
                
    while pc_score!=0 and pc_score<17:
        pc.append(deal_card())
        print("    Dealer's cards:",pc,"score:",pc_score)
        pc_score=calculate_score(pc)
    
    print("\n    Your final hand:",player,"score:",player_score)
    print("    Dealer's final hand:",pc,"score:",pc_score)

    print(compare_score(player_score,pc_score))


repeat=""
while(1>0):
    game=input(f"Do you want to play a{repeat} game of Blackjack?\nEnter 'y' or 'n' : ").lower()

    if game=="n":
        break
    elif game=="y":
        print("\n")
    else:
        print("Please enter valid input")
        
    repeat="nother"
    play_game()

    