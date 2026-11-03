def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.

    >>> check_length('wowwhatalongpasswordgollygeewhizz')
    True

    >>> check_length('hoi')
    False
    """
    return len(password) > 7


def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.

    >>> check_letter('AardappelTester')
    True

    >>> check_letter('hoi')
    False
    """
    cap_count = 0
    low_count = 0
    for c in password:
        if c.isupper():
            if low_count > 0:
                return True
            cap_count += 1
        elif c.islower():
            if cap_count > 0:
                return True

    return False


def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.

    >>> check_number('123')
    True

    >>> check_number('hoi')
    False
    """
    for c in password:
        if c.isdigit():
            return True

    return False


def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.

    >>> check_password('AardappelTester123')
    True

    >>> check_password('hoi')
    False
    """
    return check_length(password) and check_letter(password) and check_number(password)


if __name__ == "__main__":
    u_password = input("Geef een wachtwoord: ")

    print(
        "Het gegeven wachtwoord is valide."
        if check_password(password=u_password)
        else "Het gegeven wachtwoord is niet valide."
    )
