import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Pufi", "cat", "meow")

    def test_checking_all_init(self):
        self.assertEqual("Pufi", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Pufi makes meow", self.mammal.make_sound())

    def test_info(self):
        self.assertEqual("Pufi is of type cat", self.mammal.info())


if __name__ == "__main__":
    unittest.main()