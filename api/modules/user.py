import re


def is_valid_email(email: str) -> bool:
    return re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email) is not None
