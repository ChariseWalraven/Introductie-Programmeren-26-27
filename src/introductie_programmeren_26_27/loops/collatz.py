def print_collatz(n: float) -> None:
  """Print de collatz-reeks van de gegeven n
  
  >>> print_collatz(3)
  3
  10
  5
  16
  8
  4
  2
  1
  """
  while n>1:
    print(int(n))
    if n%2==0:
      n/=2
    else:
      n=n*3+1
  else:
    print(int(n))


def collatz_length(n: float) -> int:
  """Geeft de lengte van de Collatz-reeks van n terug.
  
  >>> collatz_length(3)
  8
  """
  length = 1
  while n>1:
    length+=1
    if n%2==0:
      n/=2
    else:
      n=n*3+1
    
  return length


print_collatz(3)
print(collatz_length(3))