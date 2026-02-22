import random
import string


def generate_random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def generate_random_zip() -> str:
    return "".join(random.choices(string.digits, k=5))
