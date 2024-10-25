import random
from utils.constants import NUMBERS_LIST, LETTERS_LIST, PASSWORD_LENGTH

# Logik för att generera antingen bokstäver eller siffror
def character_generator(list):
  random_number = random.randint(0, len(list) - 1)
  return list.pop(random_number)

# LOGIK: Lösenordsgenererare som ger lika chans att generera bokstäver som siffror
def password_generator():
  
  # Listor som ska itereras igenom
  numbers = NUMBERS_LIST.copy()
  letters = LETTERS_LIST.copy()


  # Variabler att generera (password length) tecken
  password = ''
  i = 0

  # Loop som skickar tillbaka antingen en siffra eller en bokstav
  while i < PASSWORD_LENGTH:
    i += 1
    number_or_letter = random.randint(0, 1)
    
    if number_or_letter == 0:
      password += character_generator(numbers)
    else:
      password += character_generator(letters)
  
  return password
