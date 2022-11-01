import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_constructor_is_correct(self):
        self.assertEqual(len(self.statistics._players), 5)

    def test_search_function_return_player(self):
        search = self.statistics.search("Semenko")
        self.assertEqual(str(search),"Semenko EDM 4 + 12 = 16")
    
    def test_search_function_returns_none(self):
        search = self.statistics.search("Cristiano Ronaldo")
        self.assertEqual(search,None)

    def test_if_given_team_give_players_correctly(self):
        s = self.statistics.team("EDM")
        self.assertEqual(len(s),3)
    
    def test_if_sort_by_goals_correct_result(self):
        s = self.statistics.top(3,SortBy.GOALS)
        ans = s[0]
        self.assertEqual(str(ans),"Lemieux PIT 45 + 54 = 99")
    
    def test_if_sort_by_points_correct_result(self):
        s = self.statistics.top(3,SortBy.POINTS)
        ans = s[0]
        self.assertEqual(str(ans),"Gretzky EDM 35 + 89 = 124")    
    
    def test_if_sort_by_assists_correct_result(self):
        s = self.statistics.top(3,SortBy.ASSISTS)
        ans = s[0]
        self.assertEqual(str(ans),"Gretzky EDM 35 + 89 = 124")    