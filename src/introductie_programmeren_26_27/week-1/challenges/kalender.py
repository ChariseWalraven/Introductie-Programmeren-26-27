# 1 januari 1800 is een woensdag
START_DAY = 3

def is_leap_year(y: int) -> bool:
    """
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    return (y%4==0 and y%100!=0) or y%400==0


def days_from_1800(month: int, year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `month` of `year`.
    De eerste dag van `month` zit hier dus niet bij.
    Gebruikt `days_from_1800_until_year` en `days_until_month`.
    """
    raise Exception('Unimplemented!')

def days_from_1800_until_year(year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `year`.
    1 januari van het nieuwe jaar is niet meegerekend.
    Gebruikt `is_leap_year`.
    
    >>> days_from_1800_until_year(1801)
    365
    
    >>> days_from_1800_until_year(1801)
    """
    days = 0

    for y in range(1800, year):
        # if y is leap year add 366 else add 356
        ily = is_leap_year(y)
        days+= 366 if ily else 365
    
    return days

def days_until_month(month: int, year: int) -> int:
    """
    Telt het aantal dagen van 1 januari van `year` tot aan `month` van `year`.
    De dagen van `month` zitten hier dus niet bij.
    Gebruikt `days_in_month`.
    """
    raise Exception('Unimplemented!')

def days_in_month(month: int, year: int) -> int:
    """
    Bepaalt het aantal dagen in `month` van `year`.
    Gebruikt `is_leap_year`.
    """
    raise Exception('Unimplemented!')

def display_calendar(month: int, year: int) -> None:
    """
    Print de kalender.
    Gebruikt `display_header` en `display_grid`.
    """
    display_header(month=month, year=year)

def display_header(month: int, year: int) -> None:
    """
    Print de koptekst van de kalender.
    
    >>> display_header(9,2022)
    Jaar: 2022
    Maand: 9
             Sep 2022          
    ---------------------------
    >>> display_header(1,2022)
    Jaar: 2022
    Maand: 1
             Jan 2022          
    ---------------------------
    >>> display_header(6,2022)
    Jaar: 2022
    Maand: 6
             Jun 2022          
    ---------------------------
    """

    year_line = f'Jaar: {year}'
    month_num_line = f'Maand: {month}'
    month_year_line = ''

    if month == 1:
        month_year_line = 'Jan'
    elif month == 2:
        month_year_line = 'Feb'
    elif month == 3:
        month_year_line = 'Mrt'
    elif month == 4:
        month_year_line = 'Apr'
    elif month == 5:
        month_year_line = 'Mei'
    elif month == 6:
        month_year_line = 'Jun'
    elif month == 7:
        month_year_line = 'Jul'
    elif month == 8:
        month_year_line = 'Aug'
    elif month == 9:
        month_year_line = 'Sep'
    elif month == 10:
        month_year_line = 'Okt'
    elif month == 11:
        month_year_line = 'Nov'
    elif month == 12:
        month_year_line = 'Dec'
    
    month_year_line=f'{month_year_line} {year}'


    print(year_line)
    print(month_num_line)
    print(f'{month_year_line:^27}')
    print('---------------------------')

def display_grid(month: int, year: int) -> None:
    """
    Print het grid van de kalender.
    Gebruikt `first_weekday_month` en `days_in_month`.
    """
    raise Exception('Unimplemented!')

def first_weekday_month(month: int, year: int) -> int:
    """
    Bepaalt de eerste weekdag van de maand.
    Gebruikt `days_from_1800`.
    """
    raise Exception('Unimplemented!')

if __name__ == '__main__':
    year = int(input("Jaar: "))
    month = int(input("Maand: "))
    display_calendar(month, year)