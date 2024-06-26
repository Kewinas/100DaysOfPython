import random
import stages
import wordlist

chosen_word = random.choice(wordlist.word_list)
lives = 6
stages.stage.reverse()
letters_used = []

display = ["_" for _ in chosen_word]

while "_" in display and lives > 0:
    guess = input("Guess the letter: ").lower()

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives -= 1
        print(stages.stage[lives])
        print(f"Wrong guess! Lives left: {lives}")
    letters_used.append(guess)
    print(f"Letters you used already: {letters_used}")

    print(" ".join(display))

if "_" not in display:
    print("You win!")
else:
    print(f"You lose!")
