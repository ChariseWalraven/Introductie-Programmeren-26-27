def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.

    >>> check_input('ATGC')
    True
    >>> check_input('atggtttctata')
    True
    >>> check_input('booyah yeheheheh whadoop')
    False
    """

    for c in dna.upper():
        if c != "A" and c != "C" and c != "G" and c != "T":
            return False
    return True


def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).

    >>> transcribe_dna_to_rna('ATGC')
    'UACG'
    >>> transcribe_dna_to_rna('atGcAgtAttGCA')
    'UACGUCAUAACGU'
    """
    rna = ""
    rna_lookup = "AUGCGTA"
    for c in dna.upper():
        ki:None|int = None
        for i in range(len(rna_lookup)):
            rc=rna_lookup[i]
            if rc == c:
                ki = i
                break

        if ki is not None:
            rna += rna_lookup[ki+1] # value key

    return rna


if __name__ == "__main__":
    u_dna = input("DNA: ")

    if check_input(dna=u_dna):
        print(f"RNA: {transcribe_dna_to_rna(dna=u_dna)}")
    else:
        print("That is not a valid DNA string")
