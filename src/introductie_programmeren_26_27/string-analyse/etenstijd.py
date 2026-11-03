def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    
    >>> meal('00:00')
    
    >>> meal('6:59')
    
    >>> meal('7:15')
    'ontbijt'
    
    >>> meal('08:00')
    'ontbijt'
    
    >>> meal('08:01')
    
    >>> meal('12:00')
    'lunch'
    
    >>> meal('12:30')
    'lunch'
    
    >>> meal('13:00')
    'lunch'
    
    >>> meal('13:01')

    >>> meal('18:00')
    'avondeten'
    
    >>> meal('18:53')
    'avondeten'
    
    >>> meal('19:01')
    
    >>> meal('22:12')

    """
    time_parts = time.split(':')
    time_in_mins = int(time_parts[0])*60+int(time_parts[1])
    if 7*60 <= time_in_mins <= 8*60:
        return 'ontbijt'
    elif 12*60 <= time_in_mins <= 13*60:
        return 'lunch'
    elif 18*60 <= time_in_mins <= 19*60:
        return 'avondeten'
    else:
        return None
        
    
    

if __name__ == '__main__':
    u_time = input('Hoe laat is het? ')
    meal_text = meal(time=u_time)
    print(f'Het is tijd voor {meal_text}' if meal_text else None)