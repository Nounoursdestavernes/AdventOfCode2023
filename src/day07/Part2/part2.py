# Description: Day 7 Part 2 of Advent of Code 2023


CARD_STRENGTH = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'T': 3,
    '9': 4,
    '8': 5,
    '7': 6,
    '6': 7,
    '5': 8,
    '4': 9,
    '3': 10,
    '2': 11,
    'J': 12
}


def strongest_card(hand: str) -> str:
    """Returns the strongest card in a hand"""
    strongest_card = ""
    strongest_value = 13
    for card in hand:
        value = CARD_STRENGTH.get(card)
        if value < strongest_value :
            strongest_card = card
            strongest_value = value

    return strongest_card

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
      
    

    if 'J' in occurences_hand1:
        occ_joker_hand1 = occurences_hand1['J']
        if occ_joker_hand1 == 5:
            del occurences_hand1['J']
            occurences_hand1['A'] = 5
        else:    
            del occurences_hand1['J']
            max_occ_hand1 = max(occurences_hand1.items(), key=lambda x: x[1])
            
            if max_occ_hand1[1] == 1:
                strong_card_label = strongest_card(hand1)
                max_occ_hand1 = (strong_card_label, 1)

            tmp_label, tmp_int = max_occ_hand1
            del occurences_hand1[tmp_label]
            occurences_hand1[tmp_label] = tmp_int + occ_joker_hand1

    if 'J' in occurences_hand2:
        occ_joker_hand2 = occurences_hand2['J']
        if occ_joker_hand2 == 5:
            del occurences_hand2['J']
            occurences_hand2['A'] = 5
        else:
            del occurences_hand2['J']
            max_occ_hand2 = max(occurences_hand2.items(), key=lambda x: x[1])

            if max_occ_hand2[1] == 1:
                strong_card_label = strongest_card(hand2)
                max_occ_hand2 = (strong_card_label, 1)

            tmp_label, tmp_int = max_occ_hand2
            del occurences_hand2[tmp_label]
            occurences_hand2[tmp_label] = tmp_int + occ_joker_hand2
    


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

        
def part2(lines: list[str]) -> int:
    """Returns the total winnings"""
    hands = []
    for line in lines:
        current_hand, current_bid = line.split()

        if len(hands) == 0:
            hands.append((current_hand, current_bid))
            continue
        
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
