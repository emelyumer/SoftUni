from project.toy_store import ToyStore
import unittest


class ToyStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.shelf1 = ToyStore()

    def test_correct_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)

    def test_add_toy_raises_shelf_doesnt_exist(self):

        with self.assertRaises(Exception) as ex:
            self.shelf1.add_toy("J", "Barbi")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)
        self.assertIn("A", self.shelf1.toy_shelf)

    def test_add_toy_raises_toy_is_already_in_shelf(self):
        self.shelf1.toy_shelf["E"] = "Barbi"

        with self.assertRaises(Exception) as ex:
            self.shelf1.add_toy("E", "Barbi")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": "Barbi",
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)

    def test_add_toy_raises_shelf_is_already_taken(self):
        self.shelf1.toy_shelf["E"] = "Barbi"

        with self.assertRaises(Exception) as ex:
            self.shelf1.add_toy("E", "Ken")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": "Barbi",
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)

    def test_add_toy_successful(self):
        self.shelf1.add_toy("G", "Ken")

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": "Ken",
        }, self.shelf1.toy_shelf)

    def test_remove_toy_raises_shelf_does_not_exist(self):
        self.shelf1.toy_shelf["A"] = "Barbi"

        with self.assertRaises(Exception) as ex:
            self.shelf1.remove_toy("H", "Ken")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        self.assertEqual({
            "A": "Barbi",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)

    def test_remove_toy_raises_toy_does_not_exist(self):
        self.shelf1.add_toy("F", "Test")
        with self.assertRaises(Exception) as ex:
            self.shelf1.remove_toy("F", "Ken")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": "Test",
            "G": None,
        }, self.shelf1.toy_shelf)

    def test_remove_toy_successful(self):
        self.shelf1.toy_shelf["A"] = "Barbi"
        self.assertEqual({
            "A": "Barbi",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)

        result = self.shelf1.remove_toy("A", "Barbi")
        self.assertEqual("Remove toy:Barbi successfully!", result)

        self.assertIsNone(self.shelf1.toy_shelf["A"])
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf1.toy_shelf)


if __name__ == "__main__":
        unittest.main()