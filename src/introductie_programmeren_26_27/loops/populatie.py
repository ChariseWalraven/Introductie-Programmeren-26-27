from fractions import Fraction

def calculate_years(start_size: int, end_size: int) -> int:
  """
  Berekent het aantal jaar dat het duurt voor de populatie om
  end_size te bereiken.
  
  >>> calculate_years(1200, 1300)
  1
  
  >>> calculate_years(200, 1400)
  25
  
  >>> calculate_years(20, 100)
  20
      
  >>> calculate_years(10, 50) # floating point error???
  20
  """
  n:Fraction = Fraction(start_size,1)
  year:int = 0
  
  while n < end_size:
    n = n+(n/3)-(n/4)
    year += 1
  
  return year
    

if __name__ == '__main__':
  u_start_size = int(input('Startgroote:'))
  while u_start_size < 9:
    u_start_size =int(input('Startgroote (>=9):'))

  u_end_size = int(input('Eindgroote:'))
  while u_start_size > u_end_size:
      u_end_size = int(input('Eindgroote (> Startgroote):'))

  print(f'Jaren: {calculate_years(start_size=u_start_size, end_size=u_end_size)}')
