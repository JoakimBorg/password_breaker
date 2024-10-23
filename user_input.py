from utils.constants import MERGED_LIST

character_list = MERGED_LIST.copy()

# INPUT: Användarens gissningar med kontroll om det är rätt antal tecken
def user_input():
  input_approved = False
  user_string = ''

  # Kontrolloop
  while input_approved == False:
    user_string = input('Din gissning: ')
    user_string_lowercase = user_string.lower()

    # Startar om loopen om antal tecken användaren skrivit in inte är 6
    if len(user_string_lowercase) != 6:
      print('')
      print('BOT: Du ska ju använda 6 tecken.')
      print('BOT: Är det så svårt att förstå!?')
      print('')
      continue
    
    # Kontroll att val av tecken är giltiga, dvs. tillhör bokstäver (a-z) och nummer (0-9)
    approved_characters = ''
    i = 0

    while i < 6:
      for x in range(0, len(character_list)):
        if user_string_lowercase[i] == character_list[x]:
          approved_characters += 'o'
          break
        
        if (x == len(character_list) - 1):
          approved_characters += 'x'

      i += 1
    
    # INFO: Berättar för användaren att det inte är rätt typ av tecken i dess input
    if approved_characters != 'oooooo':
      print('')
      print('BOT: Fel typ av tecken!')
      print('BOT: Använd små bokstäver (a-z) och nummer (0-9). Kombinera dessa fritt.')
      print('BOT: Okej!?')
      print('')
      continue
    
    # Om användaren har skrivit in ett giltigt lösenord avslutas loopen
    input_approved = True
    
  return user_string_lowercase
