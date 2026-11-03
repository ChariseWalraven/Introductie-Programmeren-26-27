def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> evaluate(1,'+',1)
    2.0
    >>> evaluate(100,'-',9)
    91.0
    >>> evaluate(4,'+',-6)
    -2.0
    >>> evaluate(4,'*',-6)
    -24.0
    >>> evaluate(3,'/',8)
    0.375
    >>> evaluate(-1,'/',-1)
    1.0
    """
    res = 0.0
    if y == '+':
        res=x+z
    elif y == '-':
        res=x-z
    elif y == '*':
        res=x*z
    else:
        res=x/z
    
    return float(res)
    
    

if __name__ == '__main__':
    u_expression = input()
    vars = u_expression.split(' ')
    u_x = int(vars[0])
    u_y = str(vars[1])
    u_z = int(vars[2])
    
    print(evaluate(x=u_x, y=u_y, z=u_z))
