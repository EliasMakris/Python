from random import seed
from random import randrange
import time

seed(time.time())


def shuffle(deck):
    deck = list(deck)
    temp_deck = set()
    for i in range(0, len(deck)):
        rand = randrange(0, len(deck))
        temp_deck.add(deck.pop(rand))
    return temp_deck


def player_draw(hand, deck):
    hand = list(hand)
    hand.append(deck.pop())
    hand = set(hand)
    return hand


def hand_value(hand):
    hand1 = list(hand.copy())
    hand1 = [hand1[i][0] for i in range(0, len(hand1))]
    for i in range(len(hand1)):
        if hand1[i] == 'ace':
            hand1.pop(i)
            hand1.append('ace')
    nums = [str(i) for i in range(2, 11)]
    sum1 = 0
    for card in hand1:
        if card in nums:
            sum1 += int(card)
        elif card != 'ace':
            sum1 += 10
        else:
            if (sum1 + 11) > 21:
                sum1 += 1
            else:
                sum1 += 11
    return sum1


def print_hand(hand):
    time.sleep(1)
    for card in hand:
        time.sleep(1)
        print(card, " ", end='')
    print('')
    return


def print_points(hand):
    time.sleep(1)
    print("\nTotal points: ", end='')
    time.sleep(1.5)
    print(hand_value(hand), "\n")
    return


def main():
    # deck --------------------------------------
    color = ['heart', 'diamond', 'club', 'spade']
    num = ['ace']
    num.extend([str(i) for i in range(2, 11)])
    num.extend(['jack', 'queen', 'king'])
    deck = {(i, j) for i in num for j in color}
    deck = shuffle(deck)
    dealer_hand = set()
    hand_player = set()
    deck = list(deck)

    # Player draws 2 cards ---------------------
    hand_player.add(deck.pop())
    hand_player = list(hand_player)
    time.sleep(1)
    print("\nPlayer's starting hand: ", end='')
    time.sleep(2)
    print(hand_player[0], ", ", end='')
    hand_player.append(deck.pop())
    time.sleep(2)
    print(hand_player[1])
    hand_player = set(hand_player)

    # Player next draws ------------------------
    lost = 0
    while True:
        time.sleep(1.5)
        ask = input("\nDraw? (Y/n) \n")
        time.sleep(1)
        if ask == "Y":
            print("\nPlayer hits!")
            time.sleep(1)
            hand_player = player_draw(hand_player, deck)
            print("\nPlayer's hand: ", end='')
            print_hand(hand_player)
            if hand_value(hand_player) > 21:
                time.sleep(1)
                print("\nPlayer busted\n")
                lost = 1
                break
            elif hand_value(hand_player) == 21:
                time.sleep(1)
                if len(hand_player) == 2:
                    print("\nA natural Black-jack")
                else:
                    print("\nBlack-jack")
                break
        elif ask == "n":
            time.sleep(1)
            print("Player stands with hand: ", end='')
            print_hand(hand_player)
            print_points(hand_player)
            break
        else:
            print("Wrong input: answer with 'Y' for drawing or 'n' for not")

    # Dealer draws if player is not busted ------
    time.sleep(2)
    while not lost:
        dealer_hand = player_draw(dealer_hand, deck)
        print('Dealer: ', end='')
        time.sleep(2)
        print_hand(dealer_hand)
        if hand_value(dealer_hand) < 17:
            if hand_value(dealer_hand) <= hand_value(hand_player):
                time.sleep(1)
                print("Dealer draws another..\n")
                time.sleep(1)
            else:
                break
        else:
            time.sleep(2)
            print("\nThe dealer must stand!\n")
            time.sleep(.5)
            print("Dealer's hand: ", end='')
            time.sleep(1)
            print_hand(dealer_hand)
            print_points(dealer_hand)
            break

    # Settlement ------------------------------
    time.sleep(1.5)
    dealer_lost = 0
    if hand_value(dealer_hand) > 21:
        print("Player wins!")
        dealer_lost = 1
    if not dealer_lost:
        if hand_value(hand_player) < hand_value(dealer_hand) or lost:
            print("The House Wins")
        elif hand_value(hand_player) == hand_value(dealer_hand):
            print("It's a tie..")
        else:
            print("Player wins!")


main()
