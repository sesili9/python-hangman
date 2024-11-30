import random

try:
    with open("words.txt","r") as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("Error The Word is not listed")
    exit()

name = input("Input Your Name Here: ")
words_guess = random.choice(words)
letters_guess = set()
attempts = 4

while attempts > 0:
    guess = input("Input Your Letter Here: ")

    if guess in letters_guess:
        print(f"You Have Guessed The Letter!")
        continue
    letters_guess.add(guess)

    if guess in words_guess:
      print("You Are Correct!")
    else:
        attempts-=1
        print(f"You Are Wrong! You Have {attempts} left.")

    dis_word =''.join([letter if letter in letters_guess else "*" for letter in words_guess] )
    print(dis_word)

    if "*" not in dis_word:
        print(f"{name} You Have won the Game!")
        result = "Winner!"
        break
else:
    print(f"{name} You Lost the game! {words_guess} was the correct word!")
    result = (""
                   
                             "LOSS!")
with open("results.txt","a") as file:
        file.write(f"{name},{result}\n")






















