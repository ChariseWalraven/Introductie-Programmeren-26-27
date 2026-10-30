# TODO: ask for clarification on why 1200 to 1300 is 1 and 10 to 50 is 20?

def calculate_years(start_size: int, end_size: int, debug:bool=False) -> int:
  """
  Berekent het aantal jaar dat het duurt voor de populatie om
  end_size te bereiken.
  
  >>> calculate_years(1200, 1300)
  1
  
  >>> calculate_years(200, 1400)
  25
  
  >>> calculate_years(20, 100)
  20
      
  >>> calculate_years(10, 50)
  20
  """
  n_start:int = start_size
  n_end:int = start_size
  year:int = 0
  
  print('year    n_start born    died    growth  n_end') if debug else None
  while n_end < end_size:
    n_start = n_end           # ending population becomes starting population for current year
    born, died = n_start//3, n_start//4
    growth = born - died
    n_end = n_start + growth  # population grows
    print(*(str(i).ljust(7) for i in (year, n_start, born, died, growth, n_end))) if debug else None
    year += 1                 # year ends
  
  return year
    

if __name__ == '__main__':
  # u_start_size = int(input('Startgroote:'))
  # while u_start_size < 9:
  #   u_start_size =int(input('Startgroote (>=9):'))

  # u_end_size = int(input('Eindgroote:'))
  # while u_start_size > u_end_size:
  #     u_end_size = int(input('Eindgroote (> Startgroote):'))
  
  u_start_size, u_end_size, debug = 1200, 1300, True
  print(f'Jaren: {calculate_years(start_size=u_start_size, end_size=u_end_size, debug=debug)}')
  
  u_start_size, u_end_size, debug = 10, 50, True
  print(f'Jaren: {calculate_years(start_size=u_start_size, end_size=u_end_size, debug=debug)}')
