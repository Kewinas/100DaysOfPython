import blackjack_ascii
import random

print(blackjack_ascii.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
gameRun = True


def give_cards(player_cards, dealer_cards):
    player = []
    dealer = []
    for _ in range(player_cards):
        player.append(random.choice(cards))
    for _ in range(dealer_cards):
        dealer.append(random.choice(cards))
    return player, dealer


def add_score(player, dealer):
    player_sum = sum(player)
    dealer_sum = sum(dealer)
    return player_sum, dealer_sum


def check_blackjack(player_score, dealer_score):
    if player_score == 21:
        return "player"
    if dealer_score == 21:
        return "dealer"
    return None


def over_21(player_score, dealer_score):
    player_over = player_score > 21
    dealer_over = dealer_score > 21

    if player_over:
        return "player"
    if dealer_over:
        return "dealer"
    return None


while gameRun:
    status = input("Do you want to play a game of Blackjack? y/n: ")
    if status.lower() == 'y':
        player, dealer = give_cards(2, 2)
        player_score, dealer_score = add_score(player, dealer)

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {dealer[0]}")

        blackjack_winner = check_blackjack(player_score, dealer_score)
        if blackjack_winner:
            if blackjack_winner == "player":
                print("You got blackjack. You win!")
            else:
                print("Computer has blackjack. You lose!")
            continue

        game_continue = True
        while game_continue:
            more = input("Do you want another card? y/n: ")
            if more.lower() == 'y':
                player.append(random.choice(cards))
                player_score = sum(player)
                print(f"Your cards: {player}, current score: {player_score}")

                if player_score > 21 and 11 in player:
                    player[player.index(11)] = 1
                    player_score = sum(player)
                    print(
                        f"Adjusted for ace: Your cards: {player}, current score: {player_score}")

                if player_score > 21:
                    print("You have over 21. You lose!")
                    game_continue = False
                    gameRun = False
                    break
            else:
                while dealer_score < 17:
                    dealer.append(random.choice(cards))
                    dealer_score = sum(dealer)
                    if dealer_score > 21 and 11 in dealer:
                        dealer[dealer.index(11)] = 1
                        dealer_score = sum(dealer)

                print(
                    f"Dealer's cards: {dealer}, dealer's score: {dealer_score}")

                if dealer_score > 21:
                    print("Dealer has over 21. You win!")
                elif dealer_score > player_score:
                    print("Dealer wins!")
                elif dealer_score < player_score:
                    print("You win!")
                else:
                    print("It's a draw!")
                game_continue = False
                gameRun = False
    elif status.lower() == 'n':
        gameRun = False
