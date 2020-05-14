from balldontlie import balldontlie, player, stats
from calculation import getplayer
import unittest

class testProject(unittest.TestCase):
    datalist = []
    totalpages = range(1, 34)
    for page in totalpages:
        datalist.append(balldontlie('https://www.balldontlie.io/api/v1/players?page=' + str(page)))
    def test_get_player(self):
        testplayer = getplayer("Stephen", "Curry")
        self.assertEquals(testplayer.firstname, "Stephen")
        self.assertEquals(testplayer.lastname, "Curry")
    def test_get_stats(self):
        lebron = player("LeBron", "James", "237")
        lebronstats = lebron.getstats(lebron, 2018)
        self.assertEqual(lebronstats.points, 26.97)
    def test_get_per(self):
        lebron = player("LeBron", "James", "237")
        lebronstats = lebron.getstats(lebron, 2018)
        self.assertEqual(lebronstats.calculate_PER(lebronstats), 31.1428)