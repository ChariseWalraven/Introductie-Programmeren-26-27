def get_collatz(n: float) -> list[int]:
  """Geeft de Collatz-reeks van n terug.
  
  >>> get_collatz(3)
  [3, 10, 5, 16, 8, 4, 2, 1]
  """
  collatz_series = []
  
  while n>1:
    collatz_series.append(int(n))
    if n%2==0:
      n/=2
    else:
      n=n*3+1
  else:
    collatz_series.append(int(n))

  return collatz_series
  

def print_collatz(n: float) -> None:
  """Print de collatz-reeks van de gegeven n
  """
  collatz = get_collatz(n=n)
  
  print(*collatz, sep='\n')


def collatz_length(n: int) -> int:
  """Geeft de lengte van de Collatz-reeks van n terug.
  
  >>> collatz_length(3)
  8
  """
  return len(get_collatz(n=n))


print_collatz(3)
print(collatz_length(3))