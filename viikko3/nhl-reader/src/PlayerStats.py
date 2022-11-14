
class PlayerStats:
    def __init__(self,reader):
        self.reader = reader

    def top_scorers_by_nationality(self,nat):
        print("Oliot:")
        self.reader.players = sorted(self.reader.players, key=lambda player: (-(player.assists+player.goals),player.name))
        players_nat = []

        for player in self.reader.players:
            if player.nationality == nat:
                players_nat.append(player)
        return players_nat