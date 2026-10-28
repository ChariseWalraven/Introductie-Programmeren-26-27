from math import floor

def travel_costs(km: int) -> float:
  """
  Bepaalt de vervoerskosten op basis van de te rijden afstand
  naar de accomodatie (tel `km` twee keer voor heen en terug).
  
  >>> travel_costs(1250)
  325.0
  
  >>> travel_costs(800)
  208.0
    
  >>> travel_costs(2159)
  561.34
  """
  # vervoerskosten = 13c/km =0.13eur/km
  # heen en weer -> km*2
  
  return km*2*0.13

def overnight_costs(nights: int) -> float:
  """
  Bepaalt de overnachtingskosten op basis van het aantal nachten
  dat je op vakantie gaat.
  
  >>> overnight_costs(5)
  300
  
  >>> overnight_costs(10)
  600
  
  >>> overnight_costs(12)
  720
  """
  # verblijfskosten 60 eur per nacht
  return nights*60

def total_costs(km: int, nights: int) -> int:
  """
  Bepaalt de totale kosten op basis van de afstand en het aantal
  nachten en rondt af naar hele euro's.
  Deze functie delegeert zoveel mogelijk werk naar de andere
  twee functies (roep die dus hier aan).
  
  >>> total_costs(1250, 5)
  625
  
  >>> total_costs(800, 10)
  808
  
  >>> total_costs(2159, 12)
  1281
  """
  return floor(travel_costs(km=km) + overnight_costs(nights=nights)) 


if __name__ == '__main__':
  u_km = int(input('Hoe ver ga je weg in kilometers? '))
  u_nights = int(input('Hoe veel nachten is je verblijf? '))
  
  print(f'Jouw vakantie kost: {total_costs(u_km, u_nights)}')