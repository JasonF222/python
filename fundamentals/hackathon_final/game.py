from classes import card
from classes.deck import Deck 
import math

class Player:
    new_player = []
    
    def __init__(self, card, name):
        self.card = card
        self.name = name
        # print(f"{self.name} drew {card.string_val} of {card.suit}")


class Opponent:
    new_opponent = []
    
    def __init__(self, card, name):
        self.card = card
        self.name = name
        # print(f"{self.name} drew {card.string_val} of {card.suit}")
    

# user.show_cards()
# user.pick_card()

user = Deck()
player = Player(user.pick_card(), "Player Name: ")
opponent = Opponent(user.pick_card(), "Opponent Name: ")


option = input("*****\n***So you wanna play WAR?***\n \n A) Add Warriors\n B) Let the WAR begin!\n E) Exit\n")

while( option != "e" or option != "E" ):
    if option == "a" or option == "A":
        player.name = input( "First Warrior: ")
        opponent.name = input( "The Mighty Opponent: ")
        new_player = Player( card, player.name)
        new_opponent = Opponent(card, opponent.name)
    elif option == "b" or option == "B":
        if player.card.point_val > opponent.card.point_val:
            print(f"*** The amazing {player.name} drew {player.card.string_val} of {player.card.suit} and unfortunately {opponent.name} drew {opponent.card.string_val} of {opponent.card.suit} \n *** {player.name} wins! ***")
        elif opponent.card.point_val > player.card.point_val:
            print(f" *** The great {opponent.name} drew {opponent.card.string_val} of {opponent.card.suit} and unfortunately {player.name} drew {player.card.string_val} of {player.card.suit} \n *** {opponent.name} wins! ***")
        else: 
            print(f"TIE GAME")

    option = input("*****\n *** CHOOSE! ***\n \n A) Add Warriors\n B) Let the WAR begin!\n E) Exit\n")