import random
from utils.constants import NUMBERS_LIST, LETTERS_LIST, PASSWORD_LENGTH

from clues.clue_letter_count import clue_letter_count
from clues.clue_reveal import clue_reveal
from clues.clue_smallest_or_largest import clue_smallest_or_largest
from clues.clue_sum import clue_sum
from clues.clue_vowel_count import clue_vowel_count

from happiness_truth_or_lie_decider import happiness_truth_or_lie_decider

used_clues = []

def clue_generator(password, known_characters):
    global used_clues

    numbers = NUMBERS_LIST.copy()
    letters = LETTERS_LIST.copy()
    random_number = random.randint(1, 5)

    if (len(used_clues) >= 5):
        used_clues = []

    if (random_number not in used_clues):
        match random_number:
            case 1:
                clue_letter_count(password, numbers)
            case 2: 
                clue_reveal(password, known_characters)
            case 3:
                clue_smallest_or_largest(password, letters, numbers)
            case 4:
                clue_sum(password)
            case 5: 
                clue_vowel_count(password)
        used_clues.append(random_number)
    else:
        clue_generator(password, known_characters)

def clue_generator_truth_or_lie(password, known_characters, bot_false_password, last_guess_true_or_false):
    #print("LAST USER GUESS FLASE/TRUE")
    #print(last_guess_true_or_false)
    truth_or_lie_clue = happiness_truth_or_lie_decider(last_guess_true_or_false)

    if (truth_or_lie_clue == 'TRUTH'):
        clue_generator(password, known_characters)
    #    print(truth_or_lie_clue)
    elif (truth_or_lie_clue == 'LIE'):
        print("(test) lie")
        clue_generator(bot_false_password, known_characters)
    #    print(truth_or_lie_clue)
