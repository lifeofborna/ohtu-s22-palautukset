class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player_score_1 = 0
        self.player_score_2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player_score_1 = self.player_score_1 + 1
        else:
            self.player_score_2 = self.player_score_2 + 1

    def get_score(self):
        score = ""

        if self.player_score_1 == self.player_score_2:
            score = self.even_score()
            return score

        if self.player_score_1 >= 4 or self.player_score_2 >= 4:
            score = self.score_grt_than_4()
            return score
        
        score = self.score_else()

        return score


    def even_score(self):
        score = ""
        even_scores = {0:'Love-All', 1:'Fifteen-All', 2:'Thirty-All',3:'Forty-All'}

        if self.player_score_1 in even_scores.keys():
            score = even_scores[self.player_score_1]
        else:
            score = "Deuce"
        
        return score
    
    def score_grt_than_4(self):
        score = ""
        score_difference = self.player_score_1 - self. player_score_2
        scores = {1:"Advantage player1", 2:'Win for player1', -1:"Advantage player2"}
        
        if score_difference in scores.keys():
            score = scores[score_difference]
        elif score_difference > 2:
            score = 'Win for player1'
        else:
            score = "Win for player2"
        return score


    def score_else(self):
        score = ""
        scores = {0:'Love', 1:'Fifteen', 2:'Thirty', 3:'Forty'}

        for i in range(1, 3):
            if i == 1:
                temp_score = self.player_score_1
            else:
                score = score + "-"
                temp_score = self.player_score_2
            
            if temp_score in scores.keys():
                score = score + scores[temp_score]
        return score