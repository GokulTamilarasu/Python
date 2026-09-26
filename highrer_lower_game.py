from game_data import data
from art import logo, vs
import random,os
#
# def compare(person1,person2,user_choice,score):
#     global continuing
#     if user_choice == 'a':
#         if person1['follower_count'] > person2['follower_count']:
#             score += 1
#             print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
#             print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
#         elif person1['follower_count'] < person2['follower_count']:
#             print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
#             print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
#             print('you loose')
#             continuing=False
#
#     else:
#         if person1['follower_count'] < person2['follower_count']:
#             score += 1
#             print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
#             print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
#         elif person1['follower_count'] > person2['follower_count']:
#             print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
#             print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
#             print('you loose')
#             continuing = False
#     return continuing,score
# def play():
#     print(logo)
#     a=random.choice(data)
#     b=random.choice(data)
#     print(f"Compare A:{a['name']},{a['description']},from {a['country']}")
#     print(vs)
#     print(f"Compare B:{b['name']},{b['description']},from {b['country']}")
#     choice=input("Who has more followers? Type 'A' or 'B': ")
#     compare(a, b, choice, score)
#     return score
#
# score=0
# continuing=True
# while continuing:
#     play()
# print(f'Score: {score}')
#
#
from game_data import data
from art import logo, vs
import random,os
def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    print(logo)
    a=random.choice(data)
    b=random.choice(data)
    while a == b:
        b =random.choice(data)
    print(f"Compare A: {a['name']},{a['description']},from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']},{b['description']},from {b['country']}")
    score=0
    continue_game=True
    while continue_game:
        a_follower = a['follower_count']
        b_follower = b['follower_count']
        choice = input("Who has more followers? Type 'A' or 'B':").lower()
        if a_follower > b_follower and choice == 'a':
            score += 1
            b=random.choice(data)
            while a == b:
                b = random.choice(data)
            clear_screen()
            print(logo)
            print(f"Compare A: {a['name']},{a['description']},from {a['country']}")
            print(vs)
            print(f"Compare B: {b['name']},{b['description']},from {b['country']}")
        elif a_follower < b_follower and choice == 'b':
            score += 1
            a=b
            b=random.choice(data)
            while a == b:
                b = random.choice(data)
            clear_screen()
            print(logo)
            print(f"Compare A: {a['name']},{a['description']},from {a['country']}")
            print(vs)
            print(f"Compare B: {b['name']},{b['description']},from {b['country']}")
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final Score:{score}")
            continue_game=False
    return None

play_game()