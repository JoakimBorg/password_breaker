from menu_start import menu_start
from info_user_won import info_user_won
from info_user_lost import info_user_lost
from menu_play_again import menu_play_again
from password_generator import password_generator
from rounds import rounds
from guess_compare import guess_compare
from utils.constants import NUMBER_OF_ROUNDS
#from utils.constants import PASSWORD_LENGTH


# PROGRAM: Programmets rundor och övergripande logik
def program():

  # Lösenorden
  bot_password = password_generator()
  bot_false_password = password_generator()
  user_password = '******'
  contained_characters = []
  known_password = "******"
  last_guess_true_or_false = False

  # Antal rundor och boolean för om användaren vunnit hej
  current_round = 1
  user_won = False

  # MENY: Startmeny
  menu_start()

  # LOGIK: Loop som spelar rundor så länge användaren inte vunnit eller rundorna tagit slut
  while (current_round <= NUMBER_OF_ROUNDS) and (user_won == False):
    user_password = rounds(current_round, user_password, known_password, contained_characters, bot_password, bot_false_password, last_guess_true_or_false)
    known_password, contained_characters = guess_compare(user_password, bot_password, known_password, contained_characters)

    # Kollar om senaste gissningen hade rätt eller fel för happiness math
    if (last_guess_true_or_false != known_password):
      last_guess_true_or_false = True
    else:
      last_guess_true_or_false = False

    if (user_password == bot_password):
      user_won = True

    current_round += 1
  
  # INFO: Om användare vinner/förlorar visas olika menyer
  if (user_won == True):
    info_user_won(bot_password)
  else:
    info_user_lost(bot_password)

# LOGIK: Funktionen program() körs härifrån
program()

# MENY: Menyn spela igen körs härifrån
play_again = menu_play_again()

while play_again == True:
  program()
  play_again = menu_play_again()

# INFO: Avslutat spelet
print('')
print('DET HÄR ÄR SLUTET FÖR DIG OCH DINA SLÄKTINGAR.')
