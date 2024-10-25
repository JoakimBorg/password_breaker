import random

def clue_reveal(password, known_characters):
    random_number = random.randint(0, (len(known_characters))-1)
    letter = known_characters[random_number]
    character_index = password.rfind(letter)
    return "tips: karaktären " + letter + " borde vara i plats "+str(character_index+1)+" i lösenordet"


test = ["3", "1", "h"]
print (clue_reveal("hej123", test))