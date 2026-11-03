def compare(word1: str, word2: str) -> int:
    """
    vergelijkt letters van word1 met word2 om te bepalen welke woorde 
    eerder in het woordenboek voorkomt.
    
    >>> compare('Taylor', 'Lana')
    1
    
    >>> compare('shark', 'sWoRd')
    -1
    
    >>> compare('Daantje', 'Daan')
    1
    
    >>> compare('amanda', 'Amanda')
    0
    """
    # Als woord1 eerder in het alfabet voorkomt dan is de uitkomst -1
    # Als woord2 eerder in het alfabet voorkomt dan is de uitkomst 1
    # Als de woorden gelijk zijn dan is de uitkomst 0

    result = 0 # default is dat ze gelijk zijn
    word1 = word1.lower().strip()
    word2 = word2.lower().strip()
    
    for i, l in enumerate(word1):
        if len(word2) > i:
            m = word2[i]
            # 
            if l < m:
                result = -1
                break
            elif l > m:
                result = 1
                break
        else:
            result = 1  # korter woord komt eerste
                
    return result

if __name__ == '__main__':
    u_word1 = input('Woord 1:')
    u_word2 = input('Woord 2:')
    result:int = compare(word1=u_word1, word2=u_word2)
    if result == -1:
        print(f'{u_word1} first')
    elif result == 1:
        print(f'{u_word2} first')
    else:
        print(f'No need to decide!')