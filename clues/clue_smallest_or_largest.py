import random
def clue_smallest_or_largest(password, LETTERS_LIST, NUMBERS_LIST):
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
                if (char == 'bokstaven'):
                    print("LEDTRÅD: Bokstaven (" + number_or_letter[x] + ") finns i lösenordet och är den bokstav som är tagen FÖRST ur alfabetet")
                    return
                
                print("LEDTRÅD: Den minsta "+char+ " i lösenordet är "+ number_or_letter[x])
                return
    else:
        for x in range(len(number_or_letter)):
            if(number_or_letter[len(number_or_letter)-(x+1)] in password):
                if (char == 'bokstaven'):
                    print("LEDTRÅD: Bokstaven (" + number_or_letter[x] + ") finns i lösenordet och är den bokstav som är tagen SIST ur alfabetet")
                    return

                print("LEDTRÅD: Den största "+char+ " i lösenordet är "+ number_or_letter[len(number_or_letter)-(x+1)])
                return

