# 21 card game

import random

class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

    def find_value(self):
        if isinstance(self.value, str):
            return 10 
        else:
            return self.value

    def __str__(self):
        return f"{self.value} of {self.suite}"
    
class DECK:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        values = range(2,11)
        suites = ["SPADES","HEARTS","CLUBS","DIAMONDS"]
        face_values = ["JACK","QUEEN","KING","ACE"]
        for suite in suites:
            for value in values:
                card = Card(value, suite)
                self.deck.append(card)
        for face_value in face_values:
            for suite in suites:
                card = Card(face_value, suite)
                self.deck.append(card)
        return self.deck

    def deal_card(self, amount=1):
        number_pulled = 0
        cards_delt = []
        while number_pulled < amount:
            if self.deck:
                pulled_card  = random.choice(self.deck)
                cards_delt.append(pulled_card)
                self.deck.remove(pulled_card)
                number_pulled += 1
            else:
                print("no deck")
                break
        return [card for card in cards_delt]

    def __str__(self):
       return '\n'.join(str(card) for card in self.deck)
    

class Player():
    def __init__(self):
        self.hand = []
        self.worth = 0

    def add_to_hand(self, cards=list):
        if cards:
            self.hand.extend(cards)
            for card in cards:
                self.worth += card.find_value() 
        else:
            print("no cards")

    def __str__(self):
        return f"{[str(card) for card in self.hand]}, total: {self.worth}"



    
        
my_deck = DECK()
my_deck.create_deck()
my_card = my_deck.deal_card(2)
their_card = my_deck.deal_card(2)
print(len(my_deck.deck))


player1 = Player()
player1.add_to_hand(my_card)
print(player1)

player2 = Player()
player2.add_to_hand(their_card)
print(player2)
hit = my_deck.deal_card(1)
player2.add_to_hand(hit)
print(player2)

print(len(my_deck.deck))












