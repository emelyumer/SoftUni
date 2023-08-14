from project.tennis_player import TennisPlayer
import unittest


class TennisPlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player1 = TennisPlayer("Ivan", 38, 5)
        self.player2 = TennisPlayer("Dragan", 26, 2)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.player1.name)
        self.assertEqual(38, self.player1.age)
        self.assertEqual(5, self.player1.points)
        self.assertEqual([], self.player1.wins)
        self.player2.wins.append("Wimbledon")
        self.player2.wins.append("US Open")
        self.assertEqual(["Wimbledon", "US Open"], self.player2.wins)

    def test_setter_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.name = "Iv"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player1.name = "a"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player1.name = ""
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_setter_name_correct(self):
        self.player1.name = "Leo"
        self.assertEqual("Leo", self.player1.name)

    def test_setter_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player1.age = -18
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_setter_age_correct(self):
        self.player1.age = 18
        self.assertEqual(18, self.player1.age)

        self.player1.age = 20
        self.assertEqual(20, self.player1.age)

    def test_add_new_win_already_added(self):
        self.player2.wins.append("Wimbledon")
        self.player2.wins.append("US Open")
        self.assertEqual(["Wimbledon", "US Open"], self.player2.wins)

        self.player2.add_new_win("Wimbledon")
        self.assertEqual("Wimbledon has been already added to the list of wins!", self.player2.add_new_win("Wimbledon"))
        self.assertEqual(["Wimbledon", "US Open"], self.player2.wins)

    def test_add_new_win_successful(self):
        self.player2.wins.append("Wimbledon")
        self.player2.wins.append("US Open")
        self.assertEqual(["Wimbledon", "US Open"], self.player2.wins)

        self.player2.add_new_win("Australian Open")
        self.assertEqual(["Wimbledon", "US Open", "Australian Open"], self.player2.wins)

        self.assertEqual([], self.player1.wins)
        self.player1.add_new_win("Australian Open")
        self.assertEqual(["Australian Open"], self.player1.wins)

    def test__lt__(self):
        self.player2.__lt__(self.player1)
        self.assertEqual("Ivan is a top seeded player and he/she is better than Dragan", self.player2.__lt__(self.player1))

        self.player1.__lt__(self.player2)
        self.assertEqual("Ivan is a better player than Dragan", self.player1.__lt__(self.player2))

    def test__str__(self):
        self.player1.__str__()
        self.assertEqual("Tennis Player: Ivan\nAge: 38\nPoints: 5.0\nTournaments won: ", self.player1.__str__())

        self.player2.wins.append("Wimbledon")
        self.player2.wins.append("US Open")
        self.assertEqual(["Wimbledon", "US Open"], self.player2.wins)

        self.player2.__str__()
        self.assertEqual("Tennis Player: Dragan\nAge: 26\nPoints: 2.0\nTournaments won: Wimbledon, US Open", self.player2.__str__())
