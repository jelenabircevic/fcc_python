import random
word_bank = [
    ("icecream", "Every time we hear the bell ding we run to get to the ____ truck!"),
    ("keyboard", "Typing on my ____ makes my wife annoyed."),
    ("bedding", "I change my ____ every two weeks."),
    ("blackboard", "We used to write on a ____ using white chalk."),
    ("airplane", "Buying ____ tickets months in advance really is cheaper!")
]
ROUNDS = 5
current_round = 1
used_words = []
correct = 0
while current_round <= ROUNDS:
    print()
    print(f"Round {current_round}")

    word, hint = random.choice(word_bank)
    while word in used_words:
        word, hint = random.choice(word_bank)
    used_words.append(word)
    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)

    print()
    print(scrambled_word.upper())
    print()

    guess = input("Guess the word (or type 'hint'/'skip'/'quit'):").strip().lower()

    if guess == "hint":
        print(f"Here is your hint: {hint}")
        guess = input("Guess the word (or type 'skip'/'quit'):").strip().lower()

    if guess == "quit":
        print("Thanks for playing!")
        break
    elif guess == "skip":
        print(f"Skipped! The word was '{word}'.")
    elif guess == word:
        print("✅ Correct!")
        correct += 1
    else:
        print(f"❌ Sorry, the word was '{word}'.")

    current_round += 1
print()
print(f"Final score: {correct}/{current_round - 1}")
if current_round - 1 == ROUNDS:
    if correct == 5:
        print("Flawless!")
    elif correct == 4:
        print("Near perfect!")
    elif correct == 3:
        print("Good effort")
    else:
        print("Have you tried turning it off and on again?")
else:
    print(f"Make it to the end next time!")