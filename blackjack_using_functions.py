from attachments import logo
import random

def dealer():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card=random.choice(cards)
    return random_card
def calculate(user_cards,computer_cards):
    user_total=sum(user_cards)
    computer_total=sum(computer_cards)
    return user_total,computer_total

def compare(user_total,computer_total):
    if user_total > 21 or user_total < computer_total:
        print(f'Your total is {user_total}')
        print(f"Computer's total is {computer_total}")
        print('You loose')
    elif computer_total < user_total <= 21 or computer_total > 21:
        print(f'Your total is {user_total} and computer"s total is {computer_total}')
        print('You won')

def play_blackjack():
    play=input("Do you want to play Blackjack, type 'y' or 'n'")
    print(logo)
    user_cards=[]
    computer_cards=[]
    if play== 'y':
        user_cards.append(dealer())
        user_cards.append(dealer())
        computer_cards.append(dealer())
        computer_cards.append(dealer())
        print(f"Your cards are {user_cards}")
        print(f"Computer's cards are {computer_cards[0]}")
        new_card=input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card=='y':
            user_cards.append(dealer())
            print(f"Your new card is {user_cards[2]}")
            computer_cards.append(dealer())
            user_total, computer_total = calculate(user_cards, computer_cards)
            compare(user_total,computer_total)
        else:
            user_total, computer_total = calculate(user_cards, computer_cards)
            compare(user_total, computer_total)

play_blackjack()


