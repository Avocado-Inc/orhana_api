def random_number_string(n: int = 6) -> str:
    """Generates n digit random number."""
    import random
    import math

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_string_n = ""
    for i in range(n):
        index = math.floor(random.random() * 10)
        random_string_n += str(digits[index])
    return random_string_n
