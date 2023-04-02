"""
Tests for square
"""
import unittest
from classes import (
    Document,
    Character,
    FileNameTypeError,
    CharacterTypeError,
    BackMovementExeption,
    ForwardMovementExeption,
    CharacterCompareError,
)


class ClassesTest(unittest.TestCase):
    """
    Test for classes (Document, Cursor, Character)
    """

    def test_character_insertion(self):
        """
        Test insertion
        """
        doc = Document("test")
        doc.insert("h")
        doc.insert("e")
        doc.insert("l")
        doc.insert("l")
        doc.insert("o")
        doc.insert("\n")
        doc.insert(Character("M", bold=True))
        doc.insert(Character("e", True))
        self.assertEqual(doc.string, "hello\n*M*e")
        doc.cursor.home()
        doc.insert("C")
        doc.insert("o")
        doc.insert("o")
        doc.insert("l")
        doc.insert(" ")
        self.assertEqual(doc.string, "hello\nCool *M*e")

    def test_exeptions(self):
        """
        Tests exeptions
        """
        try:
            doc = Document(1)
        except FileNameTypeError as err:
            print(err)
        doc = Document("test text file")
        try:
            doc.insert([1, 2, 3])
        except CharacterTypeError as err:
            print(err)
        with self.assertRaises(CharacterTypeError):
            doc.insert(3)
        with self.assertRaises(CharacterTypeError):
            Character(123, bold=True)
        character = Character("a", bold=True)
        self.assertEqual(bool(character == "d"), False)
        self.assertEqual(bool(character == Character("a")), True)
        try:
            bool(character == ["a"])
        except CharacterCompareError as err:
            print(err)

    def test_delete(self):
        """
        Test delete
        """
        doc = Document("test")
        doc.delete()
        doc.delete()
        doc.delete()
        doc.insert("h")
        doc.insert("e")
        doc.insert("l")
        doc.insert("l")
        doc.insert("o")
        doc.delete()
        doc.delete()
        doc.delete()
        self.assertEqual(doc.string, "he")

    def test_cursor_movement(self):
        """
        Test cursor movement
        """
        doc = Document("test")
        doc.cursor.home()
        doc.insert("h")
        doc.insert("i")
        doc.cursor.home()
        doc.cursor.end()
        doc.cursor.back()
        doc.cursor.back()
        try:
            doc.cursor.back()
        except BackMovementExeption as err:
            print(err)
        doc.cursor.forward()
        doc.cursor.forward()
        try:
            doc.cursor.forward()
        except ForwardMovementExeption as err:
            print(err)
        doc.cursor.back()

    def test_save(self):
        """
        Test save method
        """
        doc = Document("test")
        doc.insert("h")
        doc.insert("i")
        doc.save()


unittest.main(argv=[""], verbosity=2, exit=False)
