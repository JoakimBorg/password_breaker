# Happiness scale (hs)
# 0.5 < hs < 1 --> BOT blir gladare eftersom användaren gissar fel
# 0 < hs < 0.5 --> BOT blir argare eftersom användaren gissar rätt
happiness_scale = 0.5

# Variabler som håller reda på rätt antal gissningar i rad.
correct_answers_count = 0
wrong_answers_count = 0

# Variabler som ökar exponentvärdet beroende på antal gissningar rätt/fel i rad
bot_happy_exponent = 0
bot_angry_exponent = 0

# Funktioner för att kalkylera multiplikator/divisor
def multiplier(happy_exponent, scale):
  k_multiple = 0.7
  multiple = 1 + 0.2 * k_multiple ** happy_exponent

  return round(scale * multiple, 4)

def divider(angry_exponent, scale):
  k_divisor = 0.7
  divisor = 1 + 0.25 * k_divisor ** angry_exponent

  return round(scale / divisor, 4)

def happiness_math(last_answer_correct):
  global happiness_scale
  global bot_happy_exponent
  global bot_angry_exponent

  # Återställ exponenter när värdet rör sig över gränsen 0.5
  if happiness_scale >= 0.5:
    bot_happy_exponent = 0
  elif happiness_scale < 0.5:
    bot_angry_exponent = 0

  # Höj exponentens värde vid rätt gissning
  if last_answer_correct == False and happiness_scale >= 0.5:
    bot_happy_exponent += 1
  elif last_answer_correct == True and happiness_scale < 0.5:
    bot_angry_exponent += 1

  if last_answer_correct == False and happiness_scale < 0.5:
    bot_angry_exponent -= 1
  elif last_answer_correct == True and happiness_scale >= 0.5:
    bot_happy_exponent -= 1

  # Caluclation
#  if last_answer_correct == True:
#    happiness_scale = divider(bot_angry_exponent, happiness_scale)
#  elif last_answer_correct == False:
#    happiness_scale = multiplier(bot_happy_exponent, happiness_scale)

#  return happiness_scale

happiness_math(True)

# ToDo: Inte helt färdig, ska sy ihop den sista logiken.