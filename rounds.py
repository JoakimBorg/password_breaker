from user_input import user_input
from utils.constants import NUMBER_OF_ROUNDS
from utils.constants import PASSWORD_LENGTH
from clue_generator import clue_generator, clue_generator_truth_or_lie

# INFO: Första rundan som visar spelregler
def first_round():
  print('BOT: Jag har genererat ett hemligt lösenord på '+ str(PASSWORD_LENGTH) +' tecken.')
  print('BOT: Lösenordet är: ******')
  print('BOT: Jag vet att du inte är bra nog för att gissa mitt lösenord.')
  print('BOT: Men du kan ju försöka...')
  print('BOT: Använd små bokstäver (a-z) och nummer (0-9).')
  print('')
  print('--------------------------------')
  print('')

# RUNDA: En vanlig runda som dessutom ändrar lite text vid sista rundan
def normal_round(round_number, last_user_guess, known_password, contained_characters, bot_password, bot_false_password, last_guess_true_or_false):
  if (round_number == NUMBER_OF_ROUNDS):
    print('SISTA RUNDAN! ' + str(round_number) + ' av ' + str(NUMBER_OF_ROUNDS))
  else:
    print('RUNDA ' + str(round_number) + ' av ' + str(NUMBER_OF_ROUNDS) + ':')
    
  if (round_number != 1):
    print('')
    print('BOT: Din senaste gissning var: ' + last_user_guess)
    clue_generator_truth_or_lie(bot_password, contained_characters, bot_false_password, last_guess_true_or_false)

#skriver ut alla felplacerade karaktärer ifall det finns några
  if (len(contained_characters) != 0 ):
    print("BOT: Dessa tecken ingår men är på fel plats: " + ', '.join(contained_characters))
  print('')

# LOGIK: Rundornas logik
def rounds(round_number, last_user_guess, known_password, contained_characters, bot_password, bot_false_password, last_guess_true_or_false):
  print('--------------------------------')
  print('')

  if (round_number == 1):
    first_round()
  
  normal_round(round_number, last_user_guess, known_password, contained_characters, bot_password, bot_false_password, last_guess_true_or_false)

  print('BOT: Lösenordet är ' + known_password)
  #print('REMOVE THIS: ' + bot_password)
  user_guess = user_input()
  print('')
  
  return user_guess
