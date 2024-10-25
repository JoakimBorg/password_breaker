# Happiness scale (hs)
# 0.5 < hs < 1 --> BOT blir gladare eftersom användaren gissar fel
# 0 < hs < 0.5 --> BOT blir argare eftersom användaren gissar rätt
happiness_scale = 0.5

# Variabler som ökar exponentvärdet beroende på antal gissningar rätt/fel i rad
bot_happy_exponent = 0
bot_angry_exponent = 0

# Funktioner för att kalkylera multiplikator/divisor
def multiplier(happy_exponent, scale):
  k_multiple = 0.7
  multiple = 1 + 0.2 * k_multiple ** happy_exponent

  print()
  print('BOT GETTING HAPPY: Multiplied by: ' + str(multiple))

  return round(scale * multiple, 4)

def divider(angry_exponent, scale):
  k_divisor = 0.7
  divisor = 1 + 0.25 * k_divisor ** angry_exponent

  print()
  print('BOT GETTING ANGRY: Divided by: ' + str(divisor))

  return round(scale / divisor, 4)

def happiness_math(last_answer_correct):
  global happiness_scale
  global bot_happy_exponent
  global bot_angry_exponent

  # Caluclation
  if last_answer_correct == True:
    happiness_scale = divider(bot_angry_exponent, happiness_scale)
  elif last_answer_correct == False:
    happiness_scale = multiplier(bot_happy_exponent, happiness_scale)

  # Återställ exponenter när värdet rör sig över gränsen 0.5 (ok)
  if happiness_scale >= 0.5:
    bot_angry_exponent = 0
  elif happiness_scale < 0.5:
    bot_happy_exponent = 0

  # Höj exponentens värde vid rätt gissning och hs-värde (ok)
  if last_answer_correct == False and happiness_scale >= 0.5:
    bot_happy_exponent += 1
  elif last_answer_correct == True and happiness_scale < 0.5:
    bot_angry_exponent += 1

  # Sänk exponentens värde vid fel gissning och hs-värde
  if last_answer_correct == False and happiness_scale < 0.5:
    bot_angry_exponent -= 1
  elif last_answer_correct == True and happiness_scale >= 0.5:
    bot_happy_exponent -= 1

  testing_dict = {
    'Answer': 'Correct answer' if last_answer_correct else 'Wrong answer',
    'Scale': happiness_scale,
    'Happy exp': bot_happy_exponent,
    'Angry: exp': bot_angry_exponent,
  }

  return testing_dict

#  return happiness_scale

hsA = happiness_math(True)
hsB = happiness_math(False)
hsC = happiness_math(False)

print(hsC)

# ToDo: Inte helt färdig, ska sy ihop den sista logiken.