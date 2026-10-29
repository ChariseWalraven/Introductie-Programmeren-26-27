# TODO: add at least 3 doctests per function
def count_coins(cents: int) -> int:
  """
  Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
  waarmee het bedrag `cents` kan worden teruggegeven.
  
  >>> count_coins(41)
  4
  >>> count_coins(1112)
  47
  >>> count_coins(0)
  0
  >>> count_coins(6)
  2
  >>> count_coins(0.35*100)
  2
  """
  change_num_coins = 0
  
  while cents>0:

    if cents-25>=0:
      cents-=25
    elif cents-10>=0:
      cents-=10
    elif cents-5>=0:
      cents-=5
    else:
      cents-=1
    change_num_coins+=1
    
  return change_num_coins

    
if __name__ == '__main__':
  u_amount = float(input('Hoeveel wisselgeld moet er gegeven worden? '))
  while u_amount < 0:
    u_amount = float(
      input('Hoeveel wisselgeld moet er gegeven worden? Geef een getal (geen tekst). ')
    )

  print(count_coins(cents=round(u_amount*100)))
