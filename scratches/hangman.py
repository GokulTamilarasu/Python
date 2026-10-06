import random
words_list = [
    "cicada", "dog", "run", "book", "sky",
    "code", "data", "apple", "planet", "python",
    "machine", "science", "learning", "computer", "developer",
    "algorithm", "hyperbolic", "magnificent", "intelligence", "extraordinary"
]
chosen_word=random.choice(words_list)
print(chosen_word)
placeholder=''
for letter in chosen_word:
    placeholder += '-'
print(placeholder)
found=False
correct_letters=[]
lives=6
while not found:
    display = ''
    user_guess=input("guess the letter: ").lower()
    for letter in chosen_word:
        if user_guess==letter:
            display += user_guess
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
    print(display)
    if user_guess not in chosen_word:
        lives-=1
        print('lives : ',lives)
    if '_' not in display:
        found=True
        print("you found")
    elif lives==0:
        print("you loose")
        break
