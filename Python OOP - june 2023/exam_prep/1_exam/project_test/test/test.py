from project.movie import Movie
import unittest


class MovieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Titanic", 1997, 6.0)
        self.movie2 = Movie("Monkey", 2004, 4.0)
        self.movie3 = Movie("Lolly", 2015, 8.0)

    def test_all_init(self):
        self.assertEqual("Titanic", self.movie.name)
        self.assertEqual(1997, self.movie.year)
        self.assertEqual(6.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raises(self):
        self.assertEqual("Titanic", self.movie.name)

        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

        self.assertEqual("Titanic", self.movie.name)

    def test_name_setter_successful(self):
        self.assertEqual("Titanic", self.movie.name)

        self.movie.name = "fast and furious"

        self.assertEqual("fast and furious", self.movie.name)

    def test_year_setter_raises(self):
        self.assertEqual(1997, self.movie.year)

        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(ex.exception))

        self.assertEqual(1997, self.movie.year)

    def test_year_setter_successful(self):
        self.assertEqual(1997, self.movie.year)

        self.movie.year = 2000

        self.assertEqual(2000, self.movie.year)

    def test_add_actor_name_is_already_added(self):
        self.movie.add_actor("John")
        self.assertIn("John", self.movie.actors)
        self.assertEqual(["John"], self.movie.actors)

        result = self.movie.add_actor("John")
        self.assertEqual("John is already added in the list of actors!", result)

        self.assertIn("John", self.movie.actors)

        self.movie.add_actor("Petar")
        self.assertIn("Petar", self.movie.actors)
        self.assertEqual(["John", "Petar"], self.movie.actors)

    def test__gt__(self):
        self.assertEqual('"Titanic" is better than "Monkey"', self.movie.__gt__(self.movie2))
        self.assertEqual('"Lolly" is better than "Titanic"', self.movie.__gt__(self.movie3))

    def test__repr__(self):
        self.assertEqual("Name: Titanic\n"
                         "Year of Release: 1997\n" \
                         "Rating: 6.00\n" \
                         "Cast: ", self.movie.__repr__())


        self.movie.add_actor("Leo")
        self.movie.add_actor("Kate")

        self.assertEqual("Name: Titanic\n" \
               "Year of Release: 1997\n" \
               "Rating: 6.00\n" \
               "Cast: Leo, Kate", self.movie.__repr__())


if __name__ == "__main__":
    unittest.main()