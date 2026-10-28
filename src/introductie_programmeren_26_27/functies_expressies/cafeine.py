def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
  """
  Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
    drankjes van het type koffie, thee, energie, en cola.
    
    >>> calculate_cafeine(2,1,0,0)
    225
    
    >>> calculate_cafeine(2,0,2,0)
    340
    
    >>> calculate_cafeine(0,0,0,1)
    40
    
    >>> calculate_cafeine(5,0,0,0)
    450
    
    >>> calculate_cafeine(0,0,100,2)
    8080
    
  """
  coffee_caffeine_mg:int=90
  tea_caffeine_mg:int=45
  energy_caffeine_mg:int=80
  cola_caffeine_mg:int=40
  
  coffee_caffeine = coffee_caffeine_mg*coffee
  tea_caffeine = tea_caffeine_mg*tea
  energy_caffeine = energy_caffeine_mg*energy
  cola_caffeine = cola_caffeine_mg*cola

  return coffee_caffeine + tea_caffeine + energy_caffeine + cola_caffeine
    

if __name__ == '__main__':
  u_coffee = int(input('Hoeveel koppen koffie? '))
  u_tea = int(input('Hoeveel koppen thee? '))
  u_energy = int(input('Hoeveel energiedrankjes? '))
  u_cola = int(input('Hoeveel glazen cola? '))
  
  print(f'Je krijgt {calculate_cafeine(coffee=u_coffee, tea=u_tea, energy=u_energy, cola=u_cola)} mg caffeïne binnen.')
