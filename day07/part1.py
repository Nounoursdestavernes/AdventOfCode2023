# Description: Day 7 Part 1 of Advent of Code


CARD_STRENGTH = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12
}

def compare_hands(hand1: str, hand2: str) -> int:
    """compare two hands and return 1 if hand 1 is stronger and return 2 if hand 2 is stronger and 0 if they are equals"""

    occurences_hand1 = {}
    occurences_hand2 = {}

    for card_index in range(len(hand1)):
        card1 = hand1[card_index]
        card2 = hand2[card_index]

        if card1 not in occurences_hand1:
            occurences_hand1[card1] = 0
        if card2 not in occurences_hand2:
            occurences_hand2[card2] = 0

        occurences_hand1[card1] += 1
        occurences_hand2[card2] += 1


    occurences_hand1 = list(occurences_hand1.items())
    occurences_hand1.sort(key=lambda x: x[1], reverse=True)
    max_occ_hand1 = occurences_hand1[0][1]

    if len(occurences_hand1) == 1:
        sec_max_occ_hand1 = max_occ_hand1
    else:
        sec_max_occ_hand1 = occurences_hand1[1][1]

    occurences_hand2 = list(occurences_hand2.items())
    occurences_hand2.sort(key=lambda x: x[1], reverse=True)
    max_occ_hand2 = occurences_hand2[0][1]

    if len(occurences_hand2) == 1:
        sec_max_occ_hand2 = max_occ_hand2
    else:
        sec_max_occ_hand2 = occurences_hand2[1][1]


    if max_occ_hand1 > max_occ_hand2:
        return 1
    elif max_occ_hand2 > max_occ_hand1:
        return 2
    else:
        if sec_max_occ_hand1 > sec_max_occ_hand2:
            return 1
        elif sec_max_occ_hand2 > sec_max_occ_hand1:
            return 2
        else:
            for card_index in range(len(hand1)):
                card1 = hand1[card_index]
                card2 = hand2[card_index]
                if CARD_STRENGTH.get(card1) < CARD_STRENGTH.get(card2):
                    return 1
                elif CARD_STRENGTH.get(card2) < CARD_STRENGTH.get(card1):
                    return 2
                else:
                    continue
    
    return 0

        

def solution(textfile: str) -> int:
    """Returns the total winnings"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    hands = []
    current_hand, current_bid = lines[0].split()
    hands.append((current_hand, current_bid))

    for line in lines[1:]:
        current_hand, current_bid = line.split()
        
        index = 0
        hand = hands[index][0]
        while index < len(hands) and compare_hands(current_hand, hand) == 2:
            index += 1
            if index < len(hands):
                hand = hands[index][0]

        hands.insert(index, (current_hand, current_bid))
            
    bids = 0
    for index_hand, hand in enumerate(hands):
        bids += int(hand[1]) * (len(hands) - index_hand)


    return bids