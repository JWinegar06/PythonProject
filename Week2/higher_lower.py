print("Welcome to Higher or Lower!")
import random
import os

GAMES = [
    {
        "name": "Dragon Age: Origins",
        "series": "Dragon Age",
        "year": 2009,
        "popularity": 1981,
    },
    {
        "name": "Dragon Age II",
        "series": "Dragon Age",
        "year": 2011,
        "popularity": 870,
    },
    {
        "name": "Dragon Age: Inquisition",
        "series": "Dragon Age",
        "year": 2014,
        "popularity": 1579,
    },
    {
        "name": "Dragon Age: The Veilguard",
        "series": "Dragon Age",
        "year": 2024,
        "popularity": 93,
    },
    {
        "name": "Mass Effect",
        "series": "Mass Effect",
        "year": 2007,
        "popularity": 2719,
    },
    {
        "name": "Mass Effect 2",
        "series": "Mass Effect",
        "year": 2010,
        "popularity": 3101,
    },
    {
        "name": "Mass Effect 3",
        "series": "Mass Effect",
        "year": 2012,
        "popularity": 1793,
    },
    {
        "name": "Mass Effect: Andromeda",
        "series": "Mass Effect",
        "year": 2017,
        "popularity": 1185,
    },
    {
        "name": "Mass Effect: Legendary Edition",
        "series": "Mass Effect",
        "year": 2021,
        "popularity": 3704,
    },
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_game(game):
    return f"{game['name']} ({game['series']}, {game['year']})"


def get_random_game(exclude=None):
    choices = [game for game in GAMES if game != exclude]
    return random.choice(choices)


def check_guess(guess, a, b):
    if b["popularity"] > a["popularity"]:
        return guess == "h"
    if b["popularity"] < a["popularity"]:
        return guess == "l"
    return True  # tie counts as correct


def play_game():
    score = 0
    game_a = get_random_game()
    game_b = get_random_game(exclude=game_a)

    while True:
        clear_screen()
        print("=== HIGHER OR LOWER: Dragon Age vs Mass Effect ===")
        print("Guess which game has the HIGHER popularity score.")
        print("(Popularity score = RAWG rating count snapshot)\n")

        print(f"A: {format_game(game_a)}")
        print("VS")
        print(f"B: {format_game(game_b)}\n")

        guess = input("Type 'H' for Higher or 'L' for Lower: ").strip().lower()

        if guess not in ("h", "l"):
            print("\nPlease enter H or L.")
            input("Press Enter to continue...")
            continue

        is_correct = check_guess(guess, game_a, game_b)

        if is_correct:
            score += 1
            print("\nCorrect!")
            print(
                f"{game_b['name']} has a popularity score of {game_b['popularity']}."
            )
            print(f"Your score: {score}")
            input("\nPress Enter for the next round...")

            game_a = game_b
            game_b = get_random_game(exclude=game_a)
        else:
            print("\nWrong!")
            print(f"{game_a['name']}: {game_a['popularity']}")
            print(f"{game_b['name']}: {game_b['popularity']}")
            print(f"\nFinal score: {score}")
            break


if __name__ == "__main__":
    play_game()