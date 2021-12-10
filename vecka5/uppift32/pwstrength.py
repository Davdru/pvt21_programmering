import timeit

SPECIAL_CHARS = "#%&+_-"


def contains_number(pw: str) -> bool:
    for ch in pw:
        if ch.isnumeric():
            return True
    return False


def contains_alpha(pw: str) -> bool:
    for ch in pw:
        if ch.isalpha():
            return True
    return False


def contains_special_char(pw: str) -> bool:
    for ch in pw:
        if ch in SPECIAL_CHARS:
            return True
    return False


def contains_only_valid_chars(pw: str) -> bool:
    for ch in pw:
        if not (ch.isalpha() or ch.isnumeric() or (ch in SPECIAL_CHARS)):
            return False
    return True


def compute_strength(pw: str) -> int:
    strength = 0
    if len(pw) > 10:
        strength += 1
    if contains_number(pw) and contains_alpha(pw):
        strength += 1
    if contains_special_char(pw):
        strength += 1
    if not contains_only_valid_chars(pw):
        return 0
    return strength


def compute_strength2(pw: str):
    strength = 0
    l = 0
    alpha = False
    num = False
    spec = False
    for c in pw:
        if c.isalpha():
            alpha = True
        elif c.isnumeric():
            num = True
        elif c in SPECIAL_CHARS:
            spec = True
        else:
            return 0
        l += 1
    if l > 10:
        strength += 1
    if alpha and num:
        strength += 1
    if spec:
        strength += 1
    return strength


print(timeit.timeit(lambda: compute_strength('askdfjhklsjh12198547195#'), number=1))
print(timeit.timeit(lambda: compute_strength2('askdfjhklsjh12198547195#'), number=1))
