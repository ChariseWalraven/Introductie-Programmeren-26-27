def check_answer(answer: str) -> bool:
  """
  Controleer of het antwoord op de vraag één van de opties
  42, tweeenveertig, of tweeënveertig is.
  
  >>> check_answer('42')
  True
  
  >>> check_answer('tweeenveertig')
  True
  
  >>> check_answer('tweeënveertig')
  True
  
  >>> check_answer('*')
  False
  
  >>> check_answer('🤷🏻‍♀️')
  False
  """
  
  # zou dit werken als je de ë op een ander manier invoert? 🧐
  return answer in ['42', 'tweeenveertig', 'tweeënveertig']


if __name__ == "__main__":
  u_answer = input(
    'Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij? '
  )
  
  print('Ja' if check_answer(answer=u_answer) else 'Nee')