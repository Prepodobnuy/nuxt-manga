def in_range(num: int, min: int, max: int) -> bool:
    return num > min and num < max


def clamp(num: int, from_: int, to: int) -> int:
    return max(min(num, to), from_)
