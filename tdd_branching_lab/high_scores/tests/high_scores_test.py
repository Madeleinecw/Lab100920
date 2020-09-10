import unittest

from src.high_scores import latest, highest_to_lowest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.scores = [12, 14, 15, 16, 9]

    def test_latest(self):
        self.assertEqual(9, latest(self.scores))
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(16, personal_best(self.scores))
    # Test top three from list of scores
    def  test_personal_top_three(self):
        self.assertEqual([16, 15, 14], personal_top_three(self.scores))
    # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        self.assertEqual([16, 15, 14, 12, 9], highest_to_lowest(self.scores))
    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
