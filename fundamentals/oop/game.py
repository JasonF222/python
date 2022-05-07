from classes import card
from classes.deck import Deck 
import math

class Player:
    # new_player = []
    def __init__(self, card, name):
        self.card = card
        self.name = name
        print(f"{self.name} drew {card.string_val} of {card.suit}")


class Opponent:
    # new_opponent = []
    def __init__(self, card, name):
        self.card = card
        self.name = name
        print(f"{self.name} drew {card.string_val} of {card.suit}")
    

# user.show_cards()
# user.pick_card()

user = Deck()
player = Player(user.pick_card(), "Player" )
opponent = Opponent(user.pick_card(), "Opponent")

if player.card.point_val > opponent.card.point_val:
    print(f"{player.name} wins!")
elif opponent.card.point_val > player.card.point_val:
    print(f"{opponent.name} wins!")
else: 
    print(f"TIE GAME")


# option = input("***MENU***\n A) Add a new player\n B) Play game\n E) Exit\n")

# while( option != "e" or option != "E" ):
#     if option == "a" or option == "A":
#         player.name = input( "Player1 Name: ")
#         opponent.name = input( "Player2 Name: ")
#         new_player = Player( card, player.name)
#         new_opponent = Opponent( card, opponent.name)
#     elif option == "b" or option == "B":
#         if player.card.point_val > opponent.card.point_val:
#             print(f"{player.name} wins!")
#         elif opponent.card.point_val > player.card.point_val:
#             print(f"{opponent.name} wins!")
#         else: 
#             print(f"TIE GAME")

#     option = input("***MENU***\n A) Add a new player\n B) Play game\n E) Exit\n")
