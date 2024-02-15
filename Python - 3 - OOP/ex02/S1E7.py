from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    characters = []

    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """__str__ special method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """__repr__ special method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Turns is_alive to False"""
        self.is_alive = False

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """Create character and append it to a class list"""
        character = cls(first_name, is_alive)
        cls.characters.append(character)
        return character


class Lannister(Character):
    """Representing the Lannister family."""
    characters = []

    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """__str__ special method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """__repr__ special method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Turns is_alive to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create character and append it to a class list"""
        character = cls(first_name, is_alive)
        cls.characters.append(character)
        return character
