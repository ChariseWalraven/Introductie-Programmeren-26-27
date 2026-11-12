import random
import string


def generate_virus(length: int) -> str:
    """Genereert virus DNA van `length` nucleotiden (A, C, G of T).

    >>> len(generate_virus(4)) == 4
    True

    >>> all(n in ['A','C','G','T'] for n in generate_virus(4))
    True
    """

    return "".join([("A", "C", "G", "T")[random.randint(0, 3)] for _ in range(length)])


def mutate(virus:str, i:int|None=None):
    """Muteert een willekeurige nuceotide van een virus.
    
    >>> mutate('CCAT') != 'CCAT'
    True
    """
    i = random.randint(0, len(virus) - 1) if i is None else i
    
    mutation = generate_virus(1)
     
    if mutation != virus[i]:
        virus = virus[:i] + mutation + virus[i+1:]
        return virus
    else:
        return mutate(virus, i)
    

# 3: Afsterven

# 4: Reproductie
# 5: Resistentie
# 6: Reproductiekans
# 7: Simuleren met een virusremmer

# Grafieken

print(mutate("CCAT"))
