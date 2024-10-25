def clue_sum(password):
    sum = 0
    for char in password:
        if (char.isdigit()):
            sum+=int(char)
    return sum
    
print (clue_sum("hej123"))