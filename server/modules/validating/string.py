import re
import hashlib


def is_email_valid(email: str) -> bool:
    pattern = (
        r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
        r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    )
    return re.match(pattern, email) is not None


def hash_md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()
