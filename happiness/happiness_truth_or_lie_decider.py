from happiness_math import happiness_math
import random

TRUTH = 'TRUTH'
LIE = 'LIE'

# LOGIK: Avgör om det ska bli en lögn eller en sanning
def happiness_truth_or_lie_decider(is_last_answer_correct):
  happiness_scale = happiness_math(is_last_answer_correct)

  # Gör om happiness_scale till ett värde mellan 1 och 100
  truth_or_lie_value = round(happiness_scale * 100)

  # Värden för sanningshalter i värde (standard är sometimes_truth)
  always_truth = 60         # 100% chans för sanning
  sometimes_truth = 40      # 75% chans för sanning
  half_truth = 0            # 50% chans för sanning

  # Procentvärden
  percent_always = 100      # 100%
  percent_sometimes = 75    # 75%
  percent_half = 50         # 50%

  # Slumpvärdet och procents chans för sanning (0-100)
  percentage_chance_for_truth = percent_sometimes     # Standardprocentvärde är sometimes_truth
  percentage_random = random.randint(0, 100)

  # Matcha slumvärdet med procentens chans
  if truth_or_lie_value >= always_truth:
    percentage_chance_for_truth = percent_always
  elif truth_or_lie_value >= sometimes_truth:
    percentage_chance_for_truth = percent_sometimes
  else:
    percentage_chance_for_truth = percent_half

  # Returnera värdet
  if percentage_chance_for_truth >= percentage_random:
    return TRUTH
  else:
    return LIE
