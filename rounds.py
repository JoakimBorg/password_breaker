from user_input import user_input
from utils.constants import NUMBER_OF_ROUNDS

# INFO: Första rundan som visar spelregler
def first_round():
  print('BOT: Jag har genererat ett hemligt lösenord på 6 tecken.')
  print('BOT: Lösenordet är: ******')
  print('BOT: Jag vet att du inte är bra nog för att gissa mitt lösenord.')
  print('BOT: Men du kan ju försöka...')
  print('BOT: ...din lilla tönt.')
  print('BOT: Använd små bokstäver (a-z) och nummer (0-9).')
  print('')
  print('--------------------------------')
  print('')

# RUNDA: En vanlig runda som dessutom ändrar lite text vid sista rundan
def normal_round(round_number, last_user_guess):
  if (round_number == NUMBER_OF_ROUNDS):
    print('SISTA RUNDAN! ' + str(round_number) + ' av ' + str(NUMBER_OF_ROUNDS))
  else:
    print('RUNDA ' + str(round_number) + ' av ' + str(NUMBER_OF_ROUNDS) + ':')

  if (round_number != 1):
    print('BOT: Din senaste gissning var: ' + last_user_guess)
  
  print('')

# LOGIK: Rundornas logik
def rounds(round_number, last_user_guess):
  print('--------------------------------')
  print('')

  if (round_number == 1):
    first_round()
  
  normal_round(round_number, last_user_guess)

  user_guess = user_input()
  
  return user_guess
