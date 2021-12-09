from random import *
word_list = ['hello', 'elephant', 'camel', 'mango','moon','rocket','pigeon']
rand_int = randint(0, 6)
chosen_word = []
lives = 7
chosen_word = word_list[rand_int]
temp = []
for i in range(len(chosen_word)):
    temp.append("_")
    print(temp[i], end=" ")
while True:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i in range(0,len(chosen_word)):
            if chosen_word[i] == guess:
                temp[i] = guess
        for j in temp:
            print(j,end =" ")
        if temp.count("_") == 0:
            print("You win")
            break
        else:
            continue
    else:
        lives-=1
        print("Oops,letter not in word, you lose a life")
        if lives==0:
            print("you lose")
            print("The word was",end=" ")
            for i in chosen_word:
                print(i,end="")
            break
