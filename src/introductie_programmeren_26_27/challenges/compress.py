def not_implemented():
    raise Exception("Not implemented!")


from random import randint
from sys import getsizeof
from functools import reduce

# NOTE: gekozen om gebruik te maken van tuples in plaats van lijsten zodat de inputs een vaste structuur hebben die overeenkomt met het gewenste resultaat


# Schrijf een functie compress die een lijst met integers aanneemt en comprimeert naar een lijst met paren van integers.
def compress(ints: list[int]) -> list[tuple[int, int]]:
    """Comprimeert een lijst van integers naar een lijst met paren van integers (run-length encoding)

    >>> compress([0, 0, 1, 1, 3])
    [(0, 2), (1, 2), (3, 1)]

    >>> compress([])
    []

    >>> compress([-5, -3, -2, -2, -2, -1, -1])
    [(-5, 1), (-3, 1), (-2, 3), (-1, 2)]

    """
    result: list[tuple[int, int]] = []

    # sort list so we don't end up with separate pairs accross the list
    ints.sort()

    element: int | None = None
    aantal: int = 0

    for i in ints:
        if i != element:
            # "else None" required by Python, otherwise inline conditional doesn't work
            result.append((element, aantal)) if element != None else None
            # reset
            element = i
            aantal = 0
        aantal += 1

    result.append((element, aantal)) if element != None else None

    return result


# Schrijf een functie decompress die een lijst van lijsten met twee integers aanneemt en decomprimeert naar een lijst met integers.
def decompress(compressed_ints: list[tuple[int, int]]):
    """Decomprimeert een lijst van tuples met twee integers naar een lijst met integers.

    >>> decompress([(0, 2), (1, 2), (3, 1)])
    [0, 0, 1, 1, 3]
    >>> decompress([])
    []

    >>> decompress([(-5, 1), (-3, 1), (-2, 3), (-1, 2)])
    [-5, -3, -2, -2, -2, -1, -1]

    >>> decompress([(7, 0)])
    []

    >>> decompress([(1, 2), (7, 0), (3, 1)])
    [1, 1, 3]

    >>> decompress([(1, 2), (1, 3)])
    [1, 1, 1, 1, 1]

    >>> decompress([(10**50000, 1)]) == [10**50000]  # Werkt voor grote inputs
    True
    """

    result: list[int] = [t[0] for t in compressed_ints for _ in range(t[1])]

    return result


if __name__ == "__main__":
    # Maak een hoofdprogramma dat 1000 keer een lijst van 1000 integers genereert. Elke lijst wordt door compress gehaald en het programma houdt bij wat de compressie-ratio van elk is. Uiteindelijk print het programma de gemiddelde compressie-ratio voor alle 1000 experimenten.
    compression_ratios: list[float] = []

    for l in range(1000):
        l_1000 = [randint(0, 1000) for i in range(1000)]

        l_1000_c = compress(l_1000)

        uncompressed_size, compressed_size = getsizeof(l_1000), getsizeof(l_1000_c)

        compression_ratios.append(uncompressed_size / compressed_size)

    avg_compression_ratio = reduce(
        lambda cr_sum, cr: cr_sum + cr, compression_ratios
    ) / len(compression_ratios)

    print('Gemiddelde compressie-ratio:', avg_compression_ratio)
