
def clue_letter_count(password, numbers):
    number_count = 0
    letter_count = 0
    for x in password:
        if (x in numbers):
            number_count+=1
        else:
            letter_count+=1
    print ("tips: det finns "+str(letter_count)+ " bokstäver och " +str(number_count)+" siffor i lösenordet")

