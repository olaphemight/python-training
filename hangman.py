import random
print("Welcome To Hangman Project")

word_list = ["ardvark", "baboon", "camel"]
display = []
chosen_word = random.choice(word_list)
print(chosen_word)

for _ in range(len(chosen_word)):
    display += "_"
# print(display)
print(f"{' '.join(display)}")
# for letter in chosen_word:
    
#     if letter == guess:
#         display.append(letter)
#     else:
#         display.append("_")
# print(display)





live = 6
exist = False

end_of_the_game = False
while not end_of_the_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("guessed letter already exist! ")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
        
            display[position] = letter
    
    if guess not in chosen_word:
        live -= 1
        print(f"You guess a letter {guess}, that's not in the word, Your loose a life\n{live} live left")
        if live == 0:
            end_of_the_game = True
            print("You loose")


    print(f"{' '.join(display)}")
    

    if "_" not in display:
        end_of_the_game = True
        print(f'The word is: {chosen_word}\n You Won!')







