import random
import string

from introductie_programmeren_26_27.functions import not_implemented

type Virus = str
type Viruses = list[Virus]


def generate_virus(length: int) -> Virus:
    """Genereert virus DNA van `length` nucleotiden (A, C, G of T).

    >>> len(generate_virus(4)) == 4
    True

    >>> all(n in ['A','C','G','T'] for n in generate_virus(4))
    True
    """

    return "".join([("A", "C", "G", "T")[random.randint(0, 3)] for _ in range(length)])


def mutate(virus: Virus, i: int | None = None) -> Virus:
    """Muteert een willekeurige nuceotide van een virus.

    >>> mutate('CCAT') != 'CCAT'
    True
    """
    i = random.randint(0, len(virus) - 1) if i is None else i

    mutation = generate_virus(1)

    if mutation != virus[i]:
        virus = virus[:i] + mutation + virus[i + 1 :]
        return virus
    else:
        return mutate(virus, i)


# 3: Afsterven
def kill(viruses: Viruses, mortality_prob: float) -> Viruses:
    """Kills some viruses. Returns surviving viruses 🦠

    >>> random.seed(42)  # ensure tests always run the same way
    >>> virus_length = 4
    >>> n_viruses = 100

    >>> # ongeveer 80 dienen te overleven
    >>> mort_prob = 0.2
    >>> len(kill(viruses=[generate_virus(virus_length) for _ in range(n_viruses)], mortality_prob=mort_prob))
    87
    
    >>> # ongeveer 50 dienen te overleven
    >>> mort_prob = 0.5
    >>> len(kill(viruses=[generate_virus(virus_length) for _ in range(n_viruses)], mortality_prob=mort_prob))
    53
    
    # alle overleven
    >>> mort_prob = 0.0
    >>> len(kill(viruses=[generate_virus(virus_length) for _ in range(n_viruses)], mortality_prob=mort_prob))
    100
    
    # geen overleven
    
    >>> mort_prob = 1.0
    >>> len(kill(viruses=[generate_virus(virus_length) for _ in range(n_viruses)], mortality_prob=mort_prob))
    0

    """
    return [v for v in viruses if random.random() > mortality_prob]


# 4: Reproductie
def reproduce(viruses:Viruses, mutation_prob:float, reproduction_prob:float) -> Viruses:
    """Viruses reproduce based on `reproduction_prob`. Their offspring mutate based on `mutation_prob`.
    
    Returns:
        viruses: All the viruses and their offspring 🦠🦠🦠
        
    >>> random.seed(42)
    >>> len(reproduce([generate_virus(4) for _ in range(2)], 0.2, 0.5))
    3
    """
    res = []
    for v in viruses:
        res.append(v)
        if random.random() > reproduction_prob:
            res.append(mutate(v) if random.random() > mutation_prob else v)

    return res

# 5: Resistentie
# 6: Reproductiekans
# 7: Simuleren met een virusremmer

# Grafieken