import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    generate a random 15 characters long
    ID for students
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Post init"""
        self.login = self.name[0] + self.surname.lower()
        self.id = generate_id()
