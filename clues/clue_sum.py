def clue_sum(password):
    sum = 0
    for char in password:
        if (char.isdigit()):
            sum+=int(char)
    print ("LEDTRÅD: Summan av alla siffror i lösenordet är "+str(sum))
    