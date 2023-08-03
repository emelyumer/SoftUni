import unittest
from project.student import Student

class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Ivan")
        self.student2 = Student("Petar", {"math": ["exam", "exam2"]})

    def test_all_init(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["exam", "exam2"]}, self.student2.courses)

    def test_enroll_Course_already_added(self):
        self.assertEqual({"math": ["exam", "exam2"]}, self.student2.courses)

        result = self.student2.enroll("math", ["math is fun", "asd"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"math": ["exam", "exam2", "math is fun", "asd"]}, self.student2.courses)

    def test_enroll_notes_have_been_added(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

        result = self.student.enroll("biology", ["something"])

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"biology": ["something"]}, self.student.courses)

    def test_enroll_notes_have_been_added_Y(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

        result = self.student.enroll("biology", ["something"], "Y")

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"biology": ["something"]}, self.student.courses)

    def test_enroll_Course_has_been_added(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

        result = self.student.enroll("biology", "bio", "bio2")

        self.assertEqual("Course has been added.", result)

        self.assertEqual({"biology": []}, self.student.courses)

    def test_add_notes_raises(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("biology", "bio")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_add_notes_successful(self):
        self.assertEqual("Petar", self.student2.name)
        self.assertEqual({"math": ["exam", "exam2"]}, self.student2.courses)

        self.student2.add_notes("math", "exam3")

        self.assertEqual({"math": ["exam", "exam2", "exam3"]}, self.student2.courses)

    def test_leave_course_raises(self):
        self.assertEqual("Petar", self.student2.name)
        self.assertEqual({"math": ["exam", "exam2"]}, self.student2.courses)

        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("biology")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

        self.assertEqual("Petar", self.student2.name)
        self.assertEqual({"math": ["exam", "exam2"]}, self.student2.courses)

    def test_leave_course_successful(self):
        self.assertEqual("Petar", self.student2.name)
        self.assertEqual({"math": ["exam", "exam2"]}, self.student2.courses)

        self.student2.leave_course("math")

        self.assertEqual("Petar", self.student2.name)
        self.assertEqual({}, self.student2.courses)


if __name__ == "__main__":
    unittest.main()
