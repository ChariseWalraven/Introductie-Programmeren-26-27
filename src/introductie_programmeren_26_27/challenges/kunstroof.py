# https://pyprog.proglab.nl/opdrachten/challenges/kunstroof
from io import TextIOWrapper
import os
from typing import Generator, Iterator

from introductie_programmeren_26_27.functions import not_implemented

# Het is jouw taak om voor de politie de groep van mogelijke daders zo klein mogelijk te maken op basis van onderstaande informatie.

# setup
DATA_DIR = f"./src/introductie_programmeren_26_27/challenges/data"  # what happens if this is not main? Probably an error, but that's a story for another day. Wonder how uv handles this sort of thing; I've never really done much with packages...
file_names = (
    "beroepscrimineel.csv",
    "buitenland.csv",
    "geboortedatum.csv",
    "inwoners.csv",
    "lengte.csv",
    "postcode_coordinaat.csv",
    "postcode.csv",
)

DATA_PATHS = (os.path.join(DATA_DIR, fn) for fn in file_names)

# Buitenland
# opdracht1: Bepaal de ids van de nog mogelijke daders. Gebruik hierbij eerst een list om de ids op te slaan en op te zoeken.

def filter_buitenland(suspect_ids:set, buitenland:TextIOWrapper) -> set:
    """
    >>> buitenland = open(list(DATA_PATHS)[1], "r")
    >>> len(filter_buitenland(buitenland)) == 83_745
    True
    """
    
    return suspect_ids - set(get_column(csv=buitenland, header=buitenland.readline()))


def get_column(
    csv: TextIOWrapper,
    header: str,
    column_name: str | None = None,
    separator: str = ",",
) -> Generator[str]:
    """Returns the data from `column_name` from the `csv`. If `column_name` is None, returns the first column."""
    header_internal = list(
        map(lambda h: h.split("\n")[0].strip(), header.split(separator))
    )

    i = header_internal.index(column_name) if column_name is not None else 0
    return (l.split(separator)[i].split("\n")[0].strip() for l in csv)


def get_columns(columns: list[str], **kwargs) -> Generator:
    for c in columns:
        print(c)
        column = get_column(column_name=c, **kwargs)
        print(*column)
        yield column


# Lengte
# opdracht4: Wat zijn nu de ids van de nog mogelijke daders?


# Geboortedatum
# opdracht5: Wat zijn nu de ids van de nog mogelijke daders?


# Beroepscrimineel of Gelegenheidsdief
# ¿Download data?

# GPS coordinaten
# opdracht6: Wat zijn nu de ids van de nog mogelijke daders?

# Resultaat
# opdracht7: Maak een csv bestand ‘daders.csv’ van de nog mogelijke daders met ‘id, naam’ als header.


if __name__ == "__main__":
    # open all the files
    files = list(open(P, "r") for P in DATA_PATHS)
    (
        beroepscrimineel,
        buitenland,
        geboortedatum,
        inwoners,
        lengte,
        postcode_coordinaat,
        postcode,
    ) = files

    # inwoners
    ids: set = set(
        get_column(csv=inwoners, header=inwoners.readline(), column_name="id")
    )

    # buitenland
    
    suspect_ids: set = filter_buitenland(ids, buitenland)
    
    # BUG: I don't get any lengtes. The header is the same and the index that's returned is correct, but somehow the list is empty. Maybe something to do with the generator?
    columns = ["id", "lengte"]
    ids_length = [
        list(c)
        for c in get_columns(columns=columns, csv=lengte, header=lengte.readline())
    ]

    # print(ids_length)
    assert len(suspect_ids) == 49_130

    #
    (f.close for f in files)
