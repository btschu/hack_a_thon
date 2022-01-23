from classes.deck import Deck
from classes.card import Card

bicycle = Deck()

card_points =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
card_signs =['Hearts','Clubs','Diamonds','Spades']

bicycle.random_card()
# bicycle.show_cards()

# random_point = random.choice(card_points)
# random_sign = random.choice(card_signs)
# random_card = f"{random_point} of {random_sign}"

# print("\nWar!\n")
# card =''
# card =input('Pick a card(c)\n')
# print(random_card)



# while card =='':
#     card =card.lower()
#     if card =='c':
#         card = card("C")
#     else:
#         print('Not a valid command, please try again\n')
#         card =''