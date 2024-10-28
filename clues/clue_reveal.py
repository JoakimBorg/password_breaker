import random


def clue_reveal(password, known_characters):
    if (len(known_characters) != 0):
        random_number = random.randint(0, (len(known_characters))-1)
        letter = known_characters[random_number]
        character_index = password.rfind(letter)
        print ("tips: karaktären " + letter + " borde vara i plats "+str(character_index+1)+" i lösenordet")
    else:
        print (password[random.randint(0,5)] + " finns i lösenordet")
