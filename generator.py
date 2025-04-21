import random
import string
import warnings


def check_good_pw(pw: str) -> bool:
    upper = any(char.isupper() for char in pw)
    lower = any(char.islower() for char in pw)
    number = any(char.isdigit() for char in pw)
    special = any(char in string.punctuation for char in pw)
    return upper and lower and number and special

def generate_password(length: int, seed_seq: None) -> str:
    if seed_seq:
        random.seed(seed_seq)
    # list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_"
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()_"
    selected_char = random.sample(list_of_chars, length)
    while not check_good_pw(selected_char):
        warnings.warn("change seed phrase for more secure password", UserWarning) 
    pass_str = "".join(selected_char)
    return pass_str
