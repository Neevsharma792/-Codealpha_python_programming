1
import random

# Categories with words and hints
CATEGORIES = {
    "Animals": [
        ("elephant", "A large animal with a trunk"),
        ("giraffe", "The tallest land animal"),
        ("kangaroo", "Marsupial that hops"),
        ("penguin", "A flightless bird that swims"),
        ("dolphin", "A smart marine mammal"),
    ],
    "Tech": [
        ("algorithm", "A set of instructions for solving a problem"),
        ("python", "A popular programming language"),
        ("keyboard", "You type with it"),
        ("internet", "A global network"),
        ("robot", "A machine that can be programmed"),
    ],
    "Sports": [
        ("soccer", "Played with a round ball and a goal"),
        ("basketball", "You shoot hoops in this sport"),
        ("tennis", "Played with rackets and a net"),
        ("cricket", "Popular in India, England, Australia"),
        ("boxing", "A sport involving gloves and punches"),
    ]
}

# ASCII art
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

MAX_TRIES = len(HANGMAN_PICS) - 1

def choose_category():
    print("🎯 Choose a category:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    while True:
        choice = input("Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return list(CATEGORIES.keys())[int(choice) - 1]
        print("❗ Invalid choice. Try again.")

def choose_word_and_hint(category):
    return random.choice(CATEGORIES[category])

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play_round():
    category = choose_category()
    word, hint = choose_word_and_hint(category)
    guessed_letters = set()
    wrong_guesses = 0
    hint_given = False

    print(f"\n🎮 Hangman - Category: {category}")
    print(f"You have {MAX_TRIES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_TRIES:
        print(HANGMAN_PICS[wrong_guesses])
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("🔁 Already guessed.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Nice!\n")
            if all(letter in guessed_letters for letter in word):
                print(display_word(word, guessed_letters))
                print(f"🎉 You WON! The word was: {word}")
                return True
        else:
            wrong_guesses += 1
            print(f"❌ Nope! {MAX_TRIES - wrong_guesses} tries left.\n")

            if wrong_guesses == 3 and not hint_given:
                print(f"💡 HINT: {hint}")
                hint_given = True

    print(HANGMAN_PICS[wrong_guesses])
    print(f"💀 You LOST. The word was: {word}")
    return False

def play_game():
    wins = 0
    losses = 0

    while True:
        if play_round():
            wins += 1
        else:
            losses += 1

        print(f"\n📊 Score: {wins} Wins | {losses} Losses")
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    play_game()
