# MENY: Spela igen
def menu_play_again():
  user_input = ''

  while user_input not in ('y', 'n'):
    print('')
    print('Vill du spela igen? (y/n)')
    user_input = input()

  if user_input == 'y':
    return True
  
  return False
