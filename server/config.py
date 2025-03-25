import hashlib


def read_secret() -> str:
    with open('.env') as file:
        return file.read()
    

def hash_string(s: str) -> str:
    hash = hashlib.sha256()
    hash.update(s.encode('utf-8'))
    return hash.hexdigest()


SECRET_KEY = read_secret()