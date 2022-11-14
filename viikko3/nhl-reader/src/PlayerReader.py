import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
       self.response = requests.get(url).json()
       self.players = []
       self.create_player()
    
    def create_player(self):

        for player_dict in self.response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict["nationality"]
            )

            self.players.append(player)


