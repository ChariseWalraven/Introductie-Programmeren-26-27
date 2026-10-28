def hoeveelheid_water(minuten: int) -> int:
  """
  Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
  gegeven het aantal minuten douchen.
  
  >>> hoeveelheid_water(1)
  12
  
  >>> hoeveelheid_water(10)
  120
      
  >>> hoeveelheid_water(4)
  48
  
  >>> hoeveelheid_water(3)
  36
  """
  return minuten*12

if __name__ == '__main__':
  minuten = int(input('Hoeveel minuten douche je? '))
  
  print(hoeveelheid_water(minuten=minuten))
