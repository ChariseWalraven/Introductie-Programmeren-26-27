"""
tutorial_transformatie.py

Kopieer elke functie uit de uitleg hiernaast naar dit bestand en vul daarna
de body in. Klik op de knop doctest om je werk te controleren.
"""

def kopie(s: str) -> str:
    """
    >>> kopie("hallo")
    'hallo'
    >>> kopie("")
    ''
    """
    new_string:str = ''
    for c in s:
        new_string+=c
    
    return new_string


def hoofdletters(s: str) -> str:
    """
    >>> hoofdletters("hallo")
    'HALLO'
    >>> hoofdletters("Dag 3!")
    'DAG 3!'
    """
    # in case all use of .upper is forbidden: 
    # (character is key, adjacent character is value,
    # so i+1 of character is i of value to convert to)
    alphabet_lookup:str = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    new_string:str = ''

    for c in s:
        if c.islower():
            for i in range(len(alphabet_lookup)):
                if alphabet_lookup[i]==c:
                    new_string+=alphabet_lookup[i+1]
                    continue
        else:
            # c is already upper (or is a digit or something else)
            new_string+=c
            
            
    # alternatively, if using upper on a single character is fine:
    new_string_2:str = ''
    for c in s:
        new_string_2+=c.upper()
    
    new_string=new_string_2
        
    return new_string


def spaties_naar_streepjes(s: str) -> str:
    """
    >>> spaties_naar_streepjes("hallo daar")
    'hallo_daar'
    >>> spaties_naar_streepjes("een twee drie")
    'een_twee_drie'
    """
    new_string:str = ''

    for c in s:
        new_string+= '_' if c == ' ' else c
        
    return new_string


def verberg_klinkers(s: str) -> str:
    """
    >>> verberg_klinkers("python")
    'pyth*n'
    >>> verberg_klinkers("Amsterdam")
    '*mst*rd*m'
    """
    vowels:str = 'aeiou'  # maar niet 'y'
    
    return ''.join(c if c.lower() not in vowels else '*' for c in s)


def l337sp34k(s: str) -> str:
    """
    >>> l337sp34k("leet")
    '1337'
    >>> l337sp34k("Hallo Toto!")
    'H4110 7070!'
    """
    # only do lowercase, since numbers don't have a case and the rest are
    # returned as is
    alphabet_lookup:str = 'a4e3l1o0t7'
    new_string:str = ''
    
    for c in s:
        lookup_idx:int = alphabet_lookup.find(c.lower())
        if lookup_idx != -1:
            new_string+=alphabet_lookup[lookup_idx+1]
        else:
            new_string+=c
    
    return new_string


def verberg_cijfers(s: str) -> str:
    """
    >>> verberg_cijfers("pincode 1234")
    'pincode ####'
    >>> verberg_cijfers("R2D2")
    'R#D#'
    """
    # let's see if we can manage this in one line, for funsies :)

    return ''.join(c if not c.isdigit() else '#' for c in s) # mwuahahahahah, i did it in one go 👹



def blackout(s: str) -> str:
    """
    >>> blackout("Geheim!")
    '######!'
    >>> blackout("R2D2 is 1 robot.")
    '#2#2 ## 1 #####.'
    """
    return ''.join("#" if c.isalpha() else c for c in s )



def replace_char(s: str, c1: str, c2: str) -> str:
    """
    >>> replace_char("banaan", "a", "o")
    'bonoon'
    >>> replace_char("hallo daar", " ", "_")
    'hallo_daar'
    """
    new_string:str = ''
    for c in s:
        new_string+=c2 if c==c1 else c
    
    return new_string


def zonder_spaties(s: str) -> str:
    """
    >>> zonder_spaties("hallo daar")
    'hallodaar'
    >>> zonder_spaties(" a b c ")
    'abc'
    """
    return ''.join('' if c == ' ' else c for c in s)
    


def verwijder_n(s: str) -> str:
    """
    >>> verwijder_n("banaan")
    'baaa'
    >>> verwijder_n("nu niet")
    'u iet'
    """
    # baa baa baa, ba-banana #minions 🤓🍌 (I'm not even a fan!)
    ns:str = ''  # ns = new_string; I got lazy
    
    for c in s:
        if c != 'n':
            ns+=c
    
    return ns



def kopie_met_posities(s: str) -> str:
    """
    >>> kopie_met_posities("hallo")
    'hallo'
    >>> kopie_met_posities("")
    ''
    """
    new_string:str = ''
    for i in range(len(s)):
        new_string+=s[i]
    
    return new_string


def laatste_letters(s: str) -> str:
    """
    >>> laatste_letters("hallo daar")
    'or'
    >>> laatste_letters("een twee drie")
    'nee'
    """
    last_letters:str = ''

    for i in range(len(s)):
        end_of_s:bool = i == len(s)-1
        if s[i] == ' ':
            last_letters+=s[i-1]
        elif end_of_s:
            last_letters+=s[i]

    return last_letters




def verwijder_n_eind(s: str) -> str:
    """
    >>> verwijder_n_eind("lopen en fietsen")
    'lope e fietse'
    >>> verwijder_n_eind("banaan, nu even.")
    'banaa, nu eve.'
    """
    ns:str = ''

    for i in range(len(s)):
        is_end:bool = i == len(s)-1
        is_before_space = s[i+1] in [' ',',','.'] if not is_end else False
        is_n:bool = s[i] == 'n'
        
        keep_condition = not ((is_end or is_before_space) and is_n)
        ns+=s[i] if keep_condition else ''
    
    return ns




def eerste_letters(s: str) -> str:
    """
    >>> eerste_letters("hallo daar")
    'hd'
    >>> eerste_letters("een twee drie")
    'etd'
    >>> eerste_letters("een twee drie a")
    'etda'
    """
    res=''
    for i in range(len(s)):
        is_start:bool = i==0
        is_after_space:bool = s[i-1] == ' ' if not is_start else False
        if is_start or is_after_space:
            res+=s[i]
        
    return res


def verwijder_n_begin(s: str) -> str:
    """
    >>> verwijder_n_begin("nu niet")
    'u iet'
    >>> verwijder_n_begin("banaan,nee")
    'banaan,ee'
    >>> verwijder_n_begin("nu even niet")
    'u even iet'
    >>> verwijder_n_begin("banaan;nee")
    'banaan;ee'
    >>> verwijder_n_begin("banaan! nee")
    'banaan! ee'
    >>> verwijder_n_begin("banaan:nee")
    'banaan:ee'
    >>> verwijder_n_begin("squi?ngee")
    'squi?gee'
    """
    ns:str = ''
    for i in range(len(s)):
        if i==0 and s[i]=='n':
            continue
        # account for other kinds of adjacent punctutation marks as well: '.:;?!'
        # essentially this check is 'is_after_punctuation'
        elif (
            s[i-1]==' ' or s[i-1]=='.' or
            s[i-1]==',' or s[i-1]=='!' or
            s[i-1] ==';' or s[i-1]=='?' or
            s[i-1] ==':'
        ) and s[i]=='n': # and finally check if current character is 'n'
            continue
        # default is to return the char
        ns+=s[i]
    
    return ns



def stretch(s: str) -> str:
    """
    >>> stretch('abc')
    'abbccc'
    >>> stretch('Hoi!')
    'Hooiii!!!!'
    """
    ns:str = ''
    
    for i in range(len(s)):
        c=s[i]
        ns+=c*(i+1)
    return ns


def autocorrect(s: str) -> str:
    """
    >>> autocorrect('---')
    '-'
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    """
    ns:str = ''
    for c in s:
        if ns != '':
            # dit is niet de eerste teken in ns
            if c.isalnum() or ns[-1] != c:
                # en is ook alfanumeriek, of niet gelijk aan de laatste teken
                ns+=c
        else:
            ns+=c
            
    return ns
            


def spongebob1(s: str) -> str:
    """
    >>> spongebob1('hello world!')
    'hElLo wOrLd!'
    """
    ns:str = ''
    for i in range(len(s)):
        ns+=s[i].upper() if i%2==1 else s[i]
        
    return ns


def spongebob2(s: str) -> str:
    """
    >>> spongebob2('hello world!')
    'hElLo WoRlD!'
    """
    i = 0
    ns:str = ''
    for c in s:
        i+=1 if c.isalpha() else 0
        ns+=c.upper() if i%2==0 else c
            
    
    return ns