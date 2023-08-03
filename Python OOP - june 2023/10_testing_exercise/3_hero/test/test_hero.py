import unittest
from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("hercules", 2, 8.8, 1.1)

    def test_all_init(self):
        self.assertEqual("hercules", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(8.8, self.hero.health)
        self.assertEqual(1.1, self.hero.damage)

    def test_battle_raise_Exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raise_ValueError_hero_health(self):
        hero2 = Hero("batman", 2, 8.8, 1.1)
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -1

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raise_ValueError_enemy_health(self):
        hero2 = Hero("batman", 2, 0.0, 1.1)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual("You cannot fight batman. He needs to rest", str(ex.exception))

        hero2 = Hero("picacu", 2, -1.0, 1.1)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(hero2)

        self.assertEqual("You cannot fight picacu. He needs to rest", str(ex.exception))

    def test_battle_successful_You_win(self):
        #first result
        hero2 = Hero("batman", 2, 2.2, 1.1)
        result = self.hero.battle(hero2)

        self.assertEqual(3, self.hero.level)
        self.assertEqual(11.600000000000001, self.hero.health)
        self.assertEqual(6.1, self.hero.damage)
        self.assertEqual("You win", result)

        #second result
        hero3 = Hero("batman", 2, 11.2, 10.1)
        result = self.hero.battle(hero3)

        self.assertEqual(3, self.hero.level)
        self.assertEqual(-8.599999999999998, self.hero.health)
        self.assertEqual(6.1, self.hero.damage)
        self.assertEqual(-7.099999999999998, hero3.health)
        self.assertEqual("Draw", result)

    def test_battle_successful_Draw(self):
        hero3 = Hero("batman", 2, 1.1, 10.1)
        result = self.hero.battle(hero3)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(-11.399999999999999, self.hero.health)
        self.assertEqual(1.1, self.hero.damage)
        self.assertEqual("Draw", result)


    def test_battle_successful_You_lose(self):
        # third result
        hero4 = Hero("spiderman", 2, 28.2, 10.1)
        result = self.hero.battle(hero4)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(-11.399999999999999, self.hero.health)
        self.assertEqual(1.1, self.hero.damage)
        self.assertEqual("You lose", result)


    def test_str_(self):
        self.assertEqual("Hero hercules: 2 lvl\nHealth: 8.8\nDamage: 1.1\n", self.hero.__str__())


if __name__ == "__main__":
    unittest.main()