import random
from collections import Counter

def generate_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append(rank + " of " + suit)  
    return deck

def draw_hand(deck, num_c =5):
    hand = []
    for _ in range(num_c):  
        cd = random.choice(deck)
        deck.remove(cd)
        hand.append(cd)
    return hand

def is_full_house(hand):
    ranks = []
    for cd in hand:
        rank = cd.split()[0]
        ranks.append(rank)
    rank_counts = Counter(ranks)

    counts = list(rank_counts.values())

    if 3 in counts and 2 in counts:
        return True
    else:
        return False

deck = generate_deck()
hand = draw_hand(deck)

if is_full_house(hand):
    result = "Full House"
else:
    result = "Not a Full House"

print("Drawn Hand:", hand)
print("Result:", result)
