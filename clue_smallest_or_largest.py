from utils.constants import LETTERS_LIST
from utils.constants import NUMBERS_LIST
import random
def clue_smallest_or_largest(password):
    number_or_letter = None
    smallest_or_largest = random.randint(0, 1)
    char = None

    if (random.randint(0,1) == 0):
        number_or_letter = LETTERS_LIST
        char = "bokstaven"
    else:
        number_or_letter = NUMBERS_LIST
        char = "siffran"

    if (smallest_or_largest == 0):
        for x in range(len(number_or_letter)):
            if(number_or_letter[x] in password):
                return("tips: den minsta "+char+ " i lösenordet är "+ number_or_letter[x])
    else:
        for x in range(len(number_or_letter)):
            if(number_or_letter[len(number_or_letter)-(x+1)] in password):
                return("tips: den största "+char+ " i lösenordet är "+ number_or_letter[len(number_or_letter)-(x+1)])


print(clue_smallest_or_largest("hej123"))