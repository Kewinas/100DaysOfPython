import art
import game_data
import random


def get_random_choice(data):
    selected = random.choice(data)
    return selected['name'], selected['follower_count'], selected[
        'description'], selected['country']


def print_comparison(name_1, description_1, country_1, name_2, description_2,
                     country_2):
    print(f"Compare A: {name_1}, {description_1}, from {country_1}")
    print(art.vs)
    print(f"Against B: {name_2}, {description_2}, from {country_2}")


def check_guess(follower_count_1, follower_count_2, guess):
    if (follower_count_1 > follower_count_2 and guess == "A") or (
            follower_count_1 < follower_count_2 and guess == "B"):
        return True
    return False


def game():
    gameRun = True
    score = 0
    data = game_data.data

    while gameRun:
        print(art.logo)
        print(f"Your score is: {score}")

        if score == 0:
            name_1, follower_count_1, description_1, country_1 = get_random_choice(
                data)

        name_2, follower_count_2, description_2, country_2 = get_random_choice(
            data)
        print_comparison(name_1, description_1, country_1, name_2,
                         description_2, country_2)

        guess = input("Who has more followers? A/B: ")

        if check_guess(follower_count_1, follower_count_2, guess):
            score += 1
            name_1, follower_count_1, description_1, country_1 = name_2, follower_count_2, description_2, country_2
        else:
            print(f"You lost! Your final score is {score}.")
            gameRun = False


if __name__ == "__main__":
    game()
