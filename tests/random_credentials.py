import string
from random import choice


def random_string(length: int) -> str:
    letters = string.ascii_lowercase
    return "".join(choice(letters) for _ in range(length))


def random_email(userlen: int, addrlen: int, domainlen: int) -> str:
    user = random_string(userlen)
    addr = random_string(addrlen)
    domain = random_string(domainlen)
    return f"{user}@{addr}.{domain}"
