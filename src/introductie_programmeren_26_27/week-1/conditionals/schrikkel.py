def is_schrikkel(year: int) -> bool:
  """Geeft True terug als een jaar een schrikkeljaar (leap year) is.
  
  >>> is_schrikkel(2024)
  True
  >>> is_schrikkel(2023)
  False
  >>> is_schrikkel(1900)
  False
  >>> is_schrikkel(2000)
  True
  """
  return (year%4==0 and year%100!=0) or year%400==0

if __name__ == "__main__":
  u_year = int(input('Vul een jaar in: '))
  
  print(f'{u_year} is {'een' if is_schrikkel(year=u_year) else 'geen'} schrikkeljaar')