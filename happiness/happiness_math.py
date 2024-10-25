# Happiness scale (HS)
# 0.5 < HS < 1 --> BOT blir gladare eftersom användaren gissar fel
# 0 < HS < 0.5 --> BOT blir argare eftersom användaren gissar rätt
happiness_scale = 0.5

# Variabler som ökar exponentvärdet beroende på antal gissningar rätt/fel i rad
bot_happy_exponent = 0
bot_angry_exponent = 0

# LOGIK: Funktioner för att kalkylera multiplikator/divisor
def multiplier(happy_exponent, scale):
  k_multiple = 0.7
  multiple = 1 + 0.2 * k_multiple ** happy_exponent

  return round(scale * multiple, 4)

def divider(angry_exponent, scale):
  k_divisor = 0.7
  divisor = 1 + 0.25 * k_divisor ** angry_exponent

  return round(scale / divisor, 4)

# LOGIK: Tar input om gissningen var rätt eller inte och skickar tillbaka ett värde för HS
def happiness_math(is_last_answer_correct):
  global happiness_scale
  global bot_happy_exponent
  global bot_angry_exponent

  # Caluclation
  if is_last_answer_correct == True:
    happiness_scale = divider(bot_angry_exponent, happiness_scale)
  elif is_last_answer_correct == False:
    happiness_scale = multiplier(bot_happy_exponent, happiness_scale)

  # Återställ exponenter när värdet rör sig över gränsen 0.5 (ok)
  if happiness_scale >= 0.5:
    bot_angry_exponent = 0
  elif happiness_scale < 0.5:
    bot_happy_exponent = 0

  # Höj exponentens värde vid rätt gissning och hs-värde (ok)
  if is_last_answer_correct == False and happiness_scale >= 0.5:
    bot_happy_exponent += 1
  elif is_last_answer_correct == True and happiness_scale < 0.5:
    bot_angry_exponent += 1

  # Sänk exponentens värde vid fel gissning och hs-värde
  if is_last_answer_correct == False and happiness_scale < 0.5:
    bot_angry_exponent -= 1
  elif is_last_answer_correct == True and happiness_scale >= 0.5:
    bot_happy_exponent -= 1

  return happiness_scale
