import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random string
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A dataclass of a student
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        To set login based on name and surname
        """
        self.login = f"{self.name[0]}{self.surname}"
