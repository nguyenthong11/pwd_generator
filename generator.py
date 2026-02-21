import random
import string

# list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_"
list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()_"

class PasswordGenerator:
    def __init__(self, length: int = 0, seed_seq = None, pw: str = "", check: bool = False):
        self.length = length
        self.seed_seq = seed_seq
        self.pw = pw
        self.check = check

    def check_good_pw(self) -> bool:
        upper = any(char.isupper() for char in self.pw)
        lower = any(char.islower() for char in self.pw)
        number = any(char.isdigit() for char in self.pw)
        special = any(char in string.punctuation for char in self.pw)
        self.check = upper and lower and number and special

    def generate_password(self) -> tuple[bool, str]:
        if self.seed_seq:
            random.seed(self.seed_seq)
        selected_char = random.sample(list_of_chars, self.length)
        self.pw = "".join(selected_char)
        self.check_good_pw()
