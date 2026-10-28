# Spec:
# De functie moet minimaal 3 gevarieerde en realistische doctests krijgen.

# Om het simpel te houden, mag je aannemen dat de gebruiker altijd braaf een positief getal invoert. Je hoeft dus geen foutafhandeling te implementeren voor het geval de gebruiker dat niet doet.

# Het resultaat moet er precies uitzien als de voorbeelden hierboven.


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
