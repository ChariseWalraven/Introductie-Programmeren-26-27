def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    
    >>> convert_temperature('f',0)
    -17
    >>> convert_temperature('f',2)
    -16
    >>> convert_temperature('f',4)
    -15
    >>> convert_temperature('f',6)
    -14
    >>> convert_temperature('f',8)
    -13
    """
    # C = (10F - 320) / 18
    return  int((18*old_temp+320)/10) if old_type == 'C' else int((10*old_temp-320)/18)

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    
    >>> print_table('C',0,20,5)
      C |   F
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68
    >>> print_table('F',0,10,2)
      F |   C
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12
    >>> print_table('F',0,9,3)
      F |   C
      0 | -17
      3 | -16
      6 | -14
      9 | -12
    """
    new_type = 'F' if old_type == 'C' else 'C'
    
    # tabel header
    table = f'{old_type:>3} |{new_type:>4}' 
    
    for tmp in range(begin_temp, end_temp+1, step_size):
        table += '\n'
        
        #  convert first then compose
        tmp_other = convert_temperature(old_type=old_type, old_temp=tmp)
        
        # compose
        line = f'{tmp:>3} |{tmp_other:>4}'
        table += line
        
    print(table)
    #

if __name__ == '__main__':
    u_uom = input("Welke eenheid van temperatuur (C of F)? ").upper()
    while u_uom != 'C' and u_uom != 'F':
        u_uom = input("Welke eenheid van temperatuur (C of F)? ").upper()
    u_begin_temp = int(input('Wat is de begintemperatuur? '))
    u_end_temp = int(input('Wat is de eindtemperatuur? '))
    u_step_size = int(input('Wat is de stapgrootte? '))
    while not u_step_size > 0:
        u_step_size = int(input('Wat is de stapgrootte? '))

    print_table(old_type=u_uom, begin_temp=u_begin_temp, end_temp=u_end_temp, step_size=u_step_size)
