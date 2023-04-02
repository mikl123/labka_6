"""
Classes
"""


class FileNameTypeError(Exception):
    """
    Filename exeptions
    """

    def __str__(self) -> str:
        return "Wrong type for filename, string is required."


class CharacterTypeError(Exception):
    """
    Character Exeption
    """

    def __str__(self) -> str:
        return "Wrong type for character, string is required."


class ForwardMovementExeption(Exception):
    """
    ForwardMovementExeption
    """

    def __init__(self, index, *args: object) -> None:
        self.index = index

    def __str__(self) -> str:
        return f"You can't move forward, max index '{self.index}' reached."


class BackMovementExeption(Exception):
    """
    Back movement exeption
    """

    def __init__(self, index, *args: object) -> None:
        self.index = index

    def __str__(self) -> str:
        return f"You can't move back, min index '{self.index}' reached."


class CharacterCompareError(Exception):
    """
    Character compare Exeption
    """

    def __init__(self, character_type, *args: object) -> None:
        self.character_type = character_type

    def __str__(self) -> str:
        return f"You can't compare object Character with {self.character_type}"


class Document:
    """
    class Dovument
    """

    def __init__(self, filename):
        self.characters = []
        self.cursor = Cursor(self)
        if not isinstance(filename, str):
            raise FileNameTypeError(filename)
        self.filename = filename

    @property
    def string(self):
        """
        String property getter
        """
        return "".join((str(c) for c in self.characters))

    def insert(self, character):
        """
        Insert method
        """
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.position += 1

    def delete(self):
        """
        Delete method
        """
        if 0<=self.cursor.position - 1<=len(self.characters)-1:
            del self.characters[self.cursor.position - 1]
            self.cursor.position -= 1

    def save(self):
        """
        Save function
        """
        with open(self.filename, "w") as f:
            f.write("".join(list(map(str, self.characters))))


class Cursor:
    """
    class Cursor
    """

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """
        Forward method
        """
        if len(self.document.characters) > self.position:
            self.position += 1
        else:
            raise ForwardMovementExeption(len(self.document.characters) - 1)

    def back(self):
        """
        Back mehod
        """
        if 0 < self.position:
            self.position -= 1
        else:
            raise BackMovementExeption(0)

    def home(self):
        """
        Home method
        """
        if self.position != 0:
            while self.document.characters[self.position - 1] != "\n":
                print(self.document.characters[self.position - 1] != "\n")
                self.position -= 1
                if self.position == 0:
                    break

    def end(self):
        """
        End method
        """
        while (
            self.position < len(self.document.characters)
            and self.document.characters[self.position] != "\n"
        ):
            self.position += 1


class Character:
    """
    Class Character
    """

    def __init__(self, character, bold=False, italic=False, underline=False):
        if not isinstance(character, str):
            raise CharacterTypeError
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character

    def __eq__(self, __value: object) -> bool:
        if not (isinstance(__value, str) or isinstance(__value, Character)):
            raise CharacterCompareError(type(__value))
        if self.character == __value:
            return True
        return False
