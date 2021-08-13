f = open("p054_poker.txt")
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A': 14}
hands = [(
            [(values[card[0]], card[1]) for card in line[:14].split(' ')],
            [(values[card[0]], card[1]) for card in line[15:-1].split(' ')])
            for line in f
        ]


def hand_value(hand):
    hand_values = [card[0] for card in hand]
    hand_values.sort()

    groups = []
    of_kind = [0, 0, 0, 0, 0]
    for value in set(hand_values):
        count = hand_values.count(value)
        groups.append((count, value))
        of_kind[count] += 1
    groups.sort(reverse=True)

    hex_hand = ''.join(hex(group[1])[2:]*group[0] for group in groups)
    straight = all(hand_values[i] == hand_values[0] + i for i in range(1, 5))
    flush = all(card[1] == hand[0][1] for card in hand)

    if hex_hand == 'f54321':
        straight = True
        hex_hand = '54321f'

    # Straight Flush
    if straight and flush:
        return '0x9' + hex_hand
    # Four of a kind
    elif of_kind[4] == 1:
        return '0x8' + hex_hand
    # Full House
    elif of_kind[3] == 1 and of_kind[2] == 1:
        return '0x7' + hex_hand
    # Flush
    elif flush:
        return '0x6' + hex_hand
    # Straight
    elif straight:
        return '0x5' + hex_hand
    # Three of a Kind
    elif of_kind[3] == 1:
        return '0x4' + hex_hand
    # Two Pair
    elif of_kind[2] == 2:
        return '0x3' + hex_hand
    # One Pair
    elif of_kind[2] == 1:
        return '0x2' + hex_hand
    # High Card
    else:
        return '0x1' + hex_hand


player_one_wins = 0
total = 0

for hand_set in hands:
    if int(hand_value(hand_set[0]), 0) > int(hand_value(hand_set[1]), 0):
        player_one_wins += 1
        print(hand_set[0], hand_set[1], hand_value(hand_set[0]), hand_value(hand_set[1]))
    else:
        print("Loss", hand_set[0], hand_set[1], hand_value(hand_set[0]), hand_value(hand_set[1]))
    total += 1

print(player_one_wins, total)

# a = [(values[card[0]], card[1]) for card in "2H 2D 4C 4D 4S".split(' ')]
# b = [(values[card[0]], card[1]) for card in "3C 3D 3S 9S 9D".split(' ')]
# a_value = hand_value(a)
# b_value = hand_value(b)
# print(a_value)
# print(b_value)
# print(int(hand_value(a), 0) > int(hand_value(b), 0))