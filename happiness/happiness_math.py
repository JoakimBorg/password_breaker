correct_answers_count = 0
wrong_answers_count = 0

k = 0.8

def multiplier(exponent):
  return 1 + 0.2 * k ** exponent

def divisor(exponent):
  return 1 + 0.25 * k ** exponent

m = round(multiplier(0), 4)
d = round(divisor(0), 4)

print(m)
print(0.5 * m)
#print(0.5 / d)