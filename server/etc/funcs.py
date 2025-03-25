import hashlib

def validate_string_by_length(string:str, min_length:int=0, max_length:int=10) -> bool:
    return min_length < len(string) < max_length

def get_error_message(string:str, min_length:int=0, max_length:int=10) -> str:
    if min_length > len(string):
        return 'is too short'
    return 'is too large'

def validate_int(number: int, min_length: int, max_length: int) -> int:
    return max(min_length, min(max_length, number))

def hash_string(s: str) -> str:
    hash = hashlib.sha256()
    hash.update(s.encode('utf-8'))
    return hash.hexdigest()

def is_string_len_valid(string: str, range: tuple[int, int]) -> bool:
    return range[0] < len(string) < range[1]

def clamp(number: int | float, range: tuple[int | float, int | float]) -> int | float:
    return max(range[0], min(range[1], number))
