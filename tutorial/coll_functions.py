def get_valuable_letters(min_value):
    scrabble_points = {
        "a": 1,
        "b": 3,
        "c": 5,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 3,
        "h": 4,
        "i": 2,
        "j": 4,
        "k": 3,
        "l": 3,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 2,
        "s": 2,
        "t": 2,
        "u": 4,
        "v": 4,
        "w": 5,
        "x": 8,
        "y": 8,
        "z": 4,
    }
    return len(list(filter(lambda e: e[1] >= min_value, scrabble_points.items())))


# 9.
def emmeren(ints: list[list[int]]) -> dict[int, list[list[int]]]:
    """Returns a dict with lists of some bucket something, see the doctests, dunno how to describe this.

    >>> emmeren([[1,2,3], [3,4], [4,5]])
    {3: [[1, 2, 3]], 2: [[3, 4], [4, 5]]}
    """
    return {
        k: list(filter(lambda e: len(e) == k, ints))
        for k, v in {len(l): [] for l in ints}.items()
    }
