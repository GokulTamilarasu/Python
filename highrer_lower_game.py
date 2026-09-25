from game_data import data
from art import logo,vs
import random

def compare(person1,person2,user_choice,score):
    global continuing
    if user_choice == 'a':
        if person1['follower_count'] > person2['follower_count']:
            score += 1
            print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
            print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
        elif person1['follower_count'] < person2['follower_count']:
            print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
            print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
            print('you loose')
            continuing=False

    else:
        if person1['follower_count'] < person2['follower_count']:
            score += 1
            print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
            print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
        elif person1['follower_count'] > person2['follower_count']:
            print(f"{person1['name']}'s follower count: {person1['follower_count']} ")
            print(f"{person2['name']}'s follower count: {person2['follower_count']} ")
            print('you loose')
            continuing = False
    return continuing,score




def play():
    print(logo)
    a=random.choice(data)
    b=random.choice(data)
    print(f"Compare A:{a['name']},{a['description']},from {a['country']}")
    print(vs)
    print(f"Compare B:{b['name']},{b['description']},from {b['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ")
    compare(a, b, choice, score)
    return score

score=0
continuing=True
while continuing:
    play()
print(f'Score: {score}')


