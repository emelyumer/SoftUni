class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest

class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3)
    def test_init_list_all_ints(self):
        some_integers = IntegerList(4, 5, 6)
        self.assertEqual(3, len(some_integers.get_data()))
        self.assertEqual(3, len(some_integers._IntegerList__data))

    def test_init_not_integers_are_not_added(self):
        some_integers = IntegerList(4, 5, 6.5)
        self.assertEqual(2, len(some_integers.get_data()))
        self.assertEqual([4, 5], some_integers.get_data())

    def test_get_data_return_list_with_elements(self):
        some_integers = IntegerList(4, 5, 6)
        self.assertEqual([4, 5, 6], some_integers.get_data())

    def test_add_method_not_in_not_int_raises(self):
        # at the beginning the elements are 3
        self.assertEqual(3, len(self.int_list.get_data()))

        test_data_values = [4.6, "asd", [], {}]
        for value in test_data_values:
            with self.assertRaises(ValueError) as ex:
                self.int_list.add(value)

            self.assertEqual('Element is not Integer', ex.exception.args[0])

    def test_add_method_add_int_adds_the_element(self):
        # at the beginning the elements are 3
        self.assertEqual(3, len(self.int_list.get_data()))

        self.int_list.add(5)

        self.assertEqual(4, len(self.int_list.get_data()))
        self.assertIn(5, self.int_list.get_data())
        self.assertEqual([1, 2, 3, 5], self.int_list.get_data())

    def test_remove_index_invalid_index_raises(self):
        # at the beginning the elements are 3
        self.assertEqual(3, len(self.int_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.int_list.get_data()))

    def test_remove_index_remove_element(self):
        # at the beginning the elements are 3
        self.assertEqual(3, len(self.int_list.get_data()))
        self.assertEqual(1, self.int_list.get_data()[0])

        result = self.int_list.remove_index(0)

        self.assertEqual(1, result)
        self.assertEqual(2, len(self.int_list.get_data()))
        self.assertEqual(2, self.int_list.get_data()[0])

