def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of de lengtes van de zijdes gelijk zijn
    
    >>> is_same_rectangle(7,4,7,4)
    True
    >>> is_same_rectangle(7,4,7,3)
    False
    >>> is_same_rectangle(4,4,4,4)
    True
    """
    return ax_length == bx_length and ay_length == by_length 

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of beide rechthoeken hetzelfde vierkant zijn
    
    >>> is_same_square(4,4,4,4)
    True
    >>> is_same_square(4,2,4,2)
    False
    >>> is_same_square(1,1,1,3)
    False
    >>> is_same_square(3,2,1,1)
    False
    """
    return ax_length == ay_length == bx_length == by_length

def calculate_length(c1: int, c2: int) -> int:
    """
    Berekent de lengte van een zijde op basis van twee coördinaten
    
    >>> calculate_length(0,7)
    7
    >>> calculate_length(0,4)
    4
    >>> calculate_length(6,13)
    7
    >>> calculate_length(2,6)
    4
    """
    return abs(c2-c1)

if __name__ == '__main__':
    u_ax1 = int(input('Geef de x1 van A: '))
    u_ax2 = int(input('Geef de x2 van A: '))
    u_ay1 = int(input('Geef de y1 van A: '))
    u_ay2 = int(input('Geef de y2 van A: '))

    u_bx1 = int(input('Geef de x1 van B: '))
    u_bx2 = int(input('Geef de x2 van B: '))
    u_by1 = int(input('Geef de y1 van B: '))
    u_by2 = int(input('Geef de y2 van B: '))

    ax_length = calculate_length(u_ax1, u_ax2)
    ay_length = calculate_length(u_ay1, u_ay2)
    bx_length = calculate_length(u_bx1, u_bx2)
    by_length = calculate_length(u_by1, u_by2)
  
    square_check = is_same_square(
        ax_length=ax_length, ay_length=ay_length, 
        bx_length=bx_length, by_length=by_length
    )

    rectangle_check = is_same_rectangle(
        ax_length=ax_length, ay_length=ay_length, 
        bx_length=bx_length, by_length=by_length
    )

    if square_check:
        print('De rechthoeken zijn gelijk!\nEn ze zijn ook nog vierkant!')
    elif rectangle_check:
        print('De rechthoeken zijn gelijk!')
    else:
        print('Er is niks aan :(')
