def clue_sum(password):
    sum = 0
    for char in password:
        if (char.isdigit()):
            sum+=int(char)
    print ("tips: summan av alla siffror i lösenordet är "+str(sum))
    