def is_acidic(ph: float) -> bool:
  """True als een ph een zuur is en False anders.
  
  >>> is_acidic(7.0)
  False
  
  >>> is_acidic(4.0)
  True
  
  >>> is_acidic(8.0)
  False
  
  >>> is_acidic(2.5)
  True
  """
  return bool(ph < 7.0)

if __name__ == '__main__':
  ph = float(input("Geef een pH-waarde: "))
  
  if is_acidic(ph):
    print("Het is een zuur")
  else:
    print("Het is een base")
