import re

def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    -9
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    3
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    9
    
    """
    
    # [:-1] omdat re.split(...) een lege string teruggeeft aan het eind
    sentences = len(re.split('[.!?]',text)[:-1])
    words = len(text.split(' '))
    letters = get_letter_count(text)
    
    return coleman_liau(words, sentences, letters)
    


def get_letter_count(text:str) -> int:
    """
    >>> get_letter_count("It was a bright cold day in April, and the clocks "
    ...     "were striking thirteen. Winston Smith, his chin nuzzled into "
    ...     "his breast in an effort to escape the vile wind, slipped quickly"
    ...     " through the glass doors of Victory Mansions, though not quickly"
    ...     " enough to prevent a swirl of gritty dust from entering along "
    ...     "with him.")
    250
    
    >>> get_letter_count("Congratulations! Today is your day. You're off to "
    ...     "Great Places! You're off and away!")
    65
    """
    only_letters = filter(lambda c: c.isalnum(),[*text])
    only_letters_str:str= ''.join(only_letters)
    return len(only_letters_str)
    

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    
    >>> coleman_liau(8,4,29)
    -9
    >>> coleman_liau(14,4,65)
    3
    >>> coleman_liau(65,1,72)
    -10
    >>> coleman_liau(31,1,184)
    18
    """
    L = 100*(letters/words)
    S = 100*(sentences/words)
    
    CLI = (0.0588*L)-(0.296*S)-15.8
    
    return round(CLI)


if __name__ == '__main__':
    u_text = input('Text: ')
    
    grade = calculate_grade(text=u_text)
    if grade < 1:
        print('Below Grade 1')
    elif grade > 16:
        print('Grade 16+')
    else:
        print('Grade', grade)
