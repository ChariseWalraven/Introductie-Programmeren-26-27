def get_positive_int() -> None:
  u_int = int(input('Enter a positive int: '))
  while u_int < 0:
    u_int = int(input('Enter a positive int: '))

def get_any_int_but_0() -> None:
  u_int = int(input('Enter an int except 0: '))
  while u_int != 0:
    u_int = int(input('Enter an int except 0: '))
  

def get_min_int(n:int) -> None:
  u_int = int(input(f'Enter an int larger than {n}: '))
  while u_int < n:
    u_int = int(input(f'Enter an int larger than {n}: '))
  

def get_two_different_ints() -> None:
  u_int = int(input('Enter an int: '))
  u_int2 = int(input('Enter a different int: '))
  while u_int == u_int2:
    u_int2 = int(input('Enter a different int: '))


if __name__ == '__main__':
  get_positive_int()
  get_any_int_but_0()
  get_min_int(100)
  get_two_different_ints()