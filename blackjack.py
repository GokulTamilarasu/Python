from script import logo
import random

play=input("Do you want to play game of Blackjack? Type 'y' or 'no': ")
#while play=='y':
if play=='y':
    print(logo)
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_cards=[random.choice(cards),random.choice(cards)]
    computer_cards=[random.choice(cards),random.choice(cards)]
    user_total,computer_total=0,0
    print(f'Your cards are {user_cards}')
    print(f"Computer's first card: {computer_cards[0]}")
    next_card=input("Type 'y' to get another card, type 'n' to pass: ")
    if next_card=='y':
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        user_total+=sum(user_cards)
        computer_total+=sum(computer_cards)
        print(f'Your cards are {user_cards}')
        print(f"Computer's cards are {computer_cards}")
        if user_total > 21 or user_total<computer_total:
            print(f'Your total is {user_total}')
            print(f"Computer's total is {computer_total}")
            print('You loose')
        elif computer_total<user_total<=21 or computer_total > 21:
            print(f'Your total is {user_total} and computer"s total is {computer_total}')
            print('You won')
    else:
        user_total += sum(user_cards)
        computer_total += sum(computer_cards)
        print(f"Computer's cards are {computer_cards}")
        if user_total > 21 or user_total<computer_total:
            print(f'Your total is {user_total}')
            print(f"Computer's total is {computer_total}")
            print('You loose')
        elif computer_total < user_total <= 21 or computer_total > 21:
            print(f'Your total is {user_total} and computer"s total is {computer_total}')
            print('You won')