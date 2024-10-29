from utils.constants import PASSWORD_LENGTH, NUMBER_OF_ROUNDS
# MENY: Startmeny
def menu_start():
  print('')
  print('-----------------------------------------------------------------------------')
  print('                     Välkommen till TOXIC PASSWORD BREAKER')
  print('-----------------------------------------------------------------------------')
  print('')
  print('Ett spel där du med hjälp av ledtrådar ska lista ut ett lösenord på '+ str(PASSWORD_LENGTH) +' tecken.')
  print('')
  print('REGLER')
  print('')
  print('1. Du har ' + str(NUMBER_OF_ROUNDS) + ' antal rundor på dig att lista ut lösenordet')
  print('2. Dina gissningar måste innehålla ' + str(PASSWORD_LENGTH) +' tecken med en blandning av små bokstäver (a-z) och siffror (0-9)')
  print('3. Du ska inte återupprepa tecken i din gissning')
  print('4. Du kommer att få ledtrådar från boten BOT')
  print('5. BOT vill absolut inte att du ska vinna, därför ljuger han ibland i ledtrådarna')
  print('')
  print('--------------------------------')
  print('')

  start_game = False

  # Loopar så länge användaren inte trycker "y"
  while start_game == False:
    print('BOT: Vill du starta spelet? (y/n)')
    user_input = input()

    if user_input != 'y':
      print('')
      print('BOT: Men din tönt? Vad gör du här om du inte trycker "y"!?')
      continue

    start_game = True

  print('')
  print('BOT: Låt oss börja...')   
  print('')
