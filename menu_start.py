# MENY: Startmeny
def menu_start():
  print('')
  print('-----------------------------------------------------------------------------')
  print('                     Välkommen till TOXIC PASSWORD BREAKER')
  print('-----------------------------------------------------------------------------')
  print('')
  print('Ett spel där du med hjälp av ledtrådar ska lista ut ett lösenord på 6 tecken.')
  print('')
  print('REGLER')
  print('')
  print('1. Du har X antal rundor på dig att lista ut lösenordet')
  print('2. Dina gissningar måste innehålla 6 tecken med en blandning av små bokstäver (a-z) och siffror (0-9)')
  print('3. Du kommer att få ledtrådar från boten BOT')
  print('4. BOT vill absolut inte att du ska vinna, därför ljuger han ibland i ledtrådarna')
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
