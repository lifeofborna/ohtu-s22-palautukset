from player_reader import PlayerReader
from enum import Enum
class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists

class Statistics:
    def __init__(self,reader):
        self.reader = reader
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many,way=None):
        if way == None or way.value == 1:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )
        elif way.value==2:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_goals
        )
        else:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_assists
        )
        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
