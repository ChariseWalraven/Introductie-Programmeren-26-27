import random

debug = True


def check_digit_presence(s: str) -> bool:
    """Returns True the first time it finds a digit in the string, otherwise returns False
    >>> check_digit_presence('0fasfasdfsdf')
    True
    >>> check_digit_presence('fdfdsfs')
    False
    >>> check_digit_presence('fas0fas1dfs0df')
    True
    """
    for c in s:
        if c.isdigit():
            return True
    return False


def get_random_letter(alphabet: str = "aeiou", seed: int | None = None) -> str:
    """Returns a random letter from the given alphabet, uses given seed if not None.

    >>> get_random_letter(seed=42)
    'a'

    >>> get_random_letter(alphabet='bcdfghjklmnpqrstvwxz', seed=42)
    'f'
    """
    if seed is not None:
        random.seed(seed)
    i = random.randint(0, len(alphabet) - 1)
    return alphabet[i]


def new_password(
    separator: str = "-",
    n_words: int = 3,
    word_length: int = 6,
    n_digits: int = 1,
    n_caps: int = 1,
) -> str | None:
    """
    Genereert een wachtwoord
    """

    # criteria:
    # 3 word like parts
    # 1 digit
    # 1 capital letter
    # separated by some symbol, '-' by default

    # calculate some stats about password
    n_separators = n_words - 1
    pwd_length = n_words * word_length + n_words - 1
    digit_probability = n_digits / word_length
    caps_probability = n_caps / word_length

    # create structure for password, '--' in case of default separator and num_words
    pwd = [c for c in separator * (n_separators)]

    # keep track of number of digits and caps
    digit_count = 0
    caps_count = 0

    words = []

    # for number of words (start with 3)
    for w_idx in range(n_words):
        # build word
        word = ""
        for i in range(word_length):
            # consonant vowel consonant vowel pattern
            # digits count as consonants (for now)
            letter = ""
            alphabet = "aeiou"
            if i % 2 == 0:
                letter = get_random_letter(alphabet=alphabet)
            else:
                if random.random() <= digit_probability and digit_count == 0:
                    alphabet = "0123456789"
                    digit_count += 1
                else:
                    alphabet = "bcdfghjklmnpqrstvwxz"

                letter = get_random_letter(alphabet=alphabet)

            if random.random() <= caps_probability and caps_count == 0:
                letter = letter.upper()
                caps_count += 1
            word += letter
        words.append(word)

    return separator.join(words)


# TODO
def print_avg_entropy() -> None:
    """
    Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
    """
    # formula is -sum(p(x) * log_2(p(x)))
    # p(x) is the probability of the given character x appearing
    # log is base 2 because we want the bit entropy
    # ???


if __name__ == "__main__":
    print(new_password())
    # print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
    # print_avg_entropy()
