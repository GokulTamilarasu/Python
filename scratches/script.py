#print(input("Welcome to the tip calculator")
#bill=float(input("What was the total bill ?"))
#tip_percent=int(input("How much tip would you like to give? 10,12 or 15?"))
#split=int(input("How many people to split the bill"))
#pay_out=((bill*(tip_percent/100))+bill)/split
#print(f'Each person should pay: ${pay_out}')
import random

#in_put=int(input("give a number"))
#if in_put%2==0:
#    print("even")
#else:
#   print("odd")

#print("welcome to python pizza deliveries ")
#size=input("what size pizza do you want? S, M or L")
#pepperoni=input("do you want pepperoni on your pizza? Y or N: ")
#extra_cheese=input("do you want extra cheese? Y or N :")
#bill=0
#if size=="S":
#    bill+=15
#    if pepperoni=="Y":
#        bill+=2
#    if extra_cheese=="Y":
#        bill+=1
#elif size=="M":
#    bill+=20
#    if pepperoni == "Y":
#        bill += 3
#    if extra_cheese == "Y":
#        bill += 1
#elif size=="L":
#    bill+=25
#    if pepperoni=="Y":
#        bill+=3
#    if extra_cheese=="Y":
#        bill+=1
#print(bill)

#import random
#random_integer=random.randint(0,10)
#if random_integer%2==0:
#    print("heads")
#else:
#    print("tails")

#import random
#friends=["alice","bob","charlie","david","emanuel"]
#random_num=random.randint(0,len(friends)-1)
#print(friends[random_num])
#print(random.choice(friends))

#import random
#ser_input=int(input("What do you choose?, 1 for Rock, 2 for Paper or 3 for Sicissors :   "))
#computer_choice=random.randint(1,3)
#computer_hand="rock"
#if computer_choice==2:
#    computer_hand="paper"
#elif computer_choice==3:
#    computer_hand="scissors"
#if user_input==computer_choice:
#    print(computer_hand)
#    print('draw the match')
#elif user_input==1 and computer_choice==2:
#    print(computer_hand)
#    print("bitch you lost lol!")
#elif user_input==1 and computer_choice==3:
#    print(computer_hand)
#    print("you won jackass")
#elif user_input==2 and computer_choice==1:
#    print(computer_hand)
#    print("you won jackass")
#elif user_input==2 and computer_choice==3:
#    print(computer_hand)
#    print("you won jackass")
#elif user_input==3 and computer_choice==1:
#    print(computer_hand)
#    print("bitch you lost lol!")
#elif user_input==3 and computer_choice==2:
#    print(computer_hand)
#    print("you won jackass")
###
#rock='''   _______
#---'   ____)
#      (_____)
#      (_____)
#      (____)
#---.__(___)

#'''

#paper='''    _______
#---'   ____)____
#          ______)
#          _______)
#         _______)
#---.__________)
#
#'''

#scissor='''    _______
#---'   ____)____
#          ______)
#       __________)
#      (____)
#---.__(___)
#'''
#user_input=int(input("What do you choose?, 1 for Rock, 2 for Paper or 3 for Sicissors : "))
#computer_choice=random.randint(1,3)
#if user_input or computer_choice == 1:
#    print(rock)
#elif user_input or computer_choice ==2:
#    print(paper)
#elif user_input or computer_choice ==3:
#    print(scissor)
#if user_input==computer_choice:
#    print('draw the match')
#elif user_input==1 and computer_choice==2:
#    print("bitch you lost lol!")
#elif user_input==1 and computer_choice==3:
#    print("you won jackass")
#elif user_input==2 and computer_choice==1:
#    print("you won jackass")
#elif user_input==2 and computer_choice==3:
#    print("you won jackass")
#elif user_input==3 and computer_choice==1:
#    print("bitch you lost lol!")
#elif user_input==3 and computer_choice==2:
#    print("you won jackass")


# import random
#
# rock='''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper='''
#    _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors='''
#    _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# signs=[rock,paper,scissors]
# user_input=int(input("What do you choose?, 1 for Rock, 2 for Paper or 3 for Sicissors : "))
# computer_choice=random.randint(1,3)
# if user_input<0 or user_input>3:
#     print("You are not choosing the given options you dumb shit ")
# else:
#     if user_input==computer_choice:
#         print("draw the match")
#     elif user_input==1 and computer_choice==2:
#         print(signs[user_input-1])
#         print("computer choice was: \n")
#         print(signs[computer_choice-1])
#         print(" You loose !")
#     elif user_input==1 and computer_choice==3:
#         print(signs[user_input-1])
#         print("computer choice was: \n")
#         print(signs[computer_choice-1])
#         print("You won !")
#     elif user_input==2 and computer_choice==1:
#         print(signs[user_input-1])
#         print("computer choice was: \n")
#         print(signs[computer_choice-1])
#         print('You won!')
#     elif user_input == 2 and computer_choice == 3:
#         print(signs[user_input - 1])
#         print("computer choice was: \n")
#         print(signs[computer_choice-1])
#         print('You loose!')
#     elif user_input == 3 and computer_choice == 1:
#         print(signs[user_input - 1])
#         print("computer choice was: \n")
#         print(signs[computer_choice-1])
#         print('You loose!')
#     elif user_input ==3 and computer_choice == 2:
#         print(signs[user_input - 1])
#         print("computer choice was: \n")
#         print(signs[computer_choice-1])
#         print('You won!')


# student_scores=[150,142,185,120,171,184,149,24,59,68,199,78,65,89]
# maximum_score=0
# for score in student_scores:
#     if score > maximum_score:
#         maximum_score=score
# print(maximum_score)

# letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
# numbers=['0','1','2','3','4','5','6','7','8','9']
# symbols=['!','#','$','%','&','(',')','*','+']
# print('Welcome to the PyPassword Generator !')
# nr_letters=int(input("how many letters would you like in your password? \n"))
# nr_symbols=int(input("how many symbols would you like in your password? \n"))
# nr_numbers=int(input("how many numbers would you like in your password? \n"))

#password=''
# for letter in range(nr_letters):
#     choice=random.choice(letters)
#     password+=choice
# for symbol in range (nr_symbols):
#     choice=random.choice(symbols)
#     password+=choice
# for  number in range (nr_numbers):
#     choice=random.choice(numbers)
#     password+=choice
# print(password)

#for absolute randomness in the password
########  method 1: can shuffle all char after generating the password
########  method 2: can use a list for the generated char and use a for loop again to get random places with random char
########  method 3: can use the same list and random.shuffle function
# password=[]
# shuffled_password=''
# for letter in range(nr_letters):
#     choice=random.choice(letters)
#     password.append(choice)
# for symbol in range (nr_symbols):
#     choice=random.choice(symbols)
#     password.append(choice)
# for  number in range (nr_numbers):
#     choice=random.choice(numbers)
#     password.append(choice)
# random.shuffle(password)
# for char in range(len(password)):
#     shuffled_password+=password[char]
# print(shuffled_password)
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
