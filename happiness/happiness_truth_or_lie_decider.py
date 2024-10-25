from happiness_math import happiness_math
import random

TRUTH = 'TRUTH'
LIE = 'LIE'

# LOGIK: Avgör om det ska bli en lögn eller en sanning
def happiness_truth_or_lie_decider(is_last_answer_correct):
  happiness_scale = happiness_math(is_last_answer_correct)

  # Gör om happiness_scale till ett värde mellan 1 och 100
  truth_or_lie_value = round(happiness_scale * 100)

  # Värdemängd för sanningshalter i värde (standard är sometimes_truth)
  always_truth = 70        # 100% chans för sanning
  sometimes_truth = 40     # 75% chans för sanning
  half_truth = 0           # 50% chans för sanning

  # Procentvärden
  percent_always = 100
  percent_sometimes = 75
  percent_half = 50

  # Slumpvärdet och procents chans för sanning (0-100)
  percentage_chance_for_truth = sometimes_truth     # Standardprocentvärde är sometimes_truth
  percentage_random = random.randint(0, 100)
  
  print('chance: ' + str(percentage_chance_for_truth))
  print('random: ' + str(percentage_random))
  print()

  # Matcha slumvärdet med procentens chans
  if truth_or_lie_value >= always_truth:
    percentage_chance_for_truth = percent_always
  elif truth_or_lie_value >= percent_sometimes:
    percentage_chance_for_truth = percent_sometimes
  else:
    percentage_chance_for_truth = percent_half

  # Returnera värdet
  if percentage_chance_for_truth >= percentage_random:
    return TRUTH
  else:
    return LIE

happiness_truth_or_lie_decider(False)
happiness_truth_or_lie_decider(False)
happiness_truth_or_lie_decider(True)
happiness_truth_or_lie_decider(True)
happiness_truth_or_lie_decider(False)
happiness_truth_or_lie_decider(False)
happiness_truth_or_lie_decider(True)
TL = happiness_truth_or_lie_decider(True)

print(TL)