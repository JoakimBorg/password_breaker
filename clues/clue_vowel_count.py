vowels = ['a','e','i','o','u']
def clue_vowel_count(password):
    vowel_count = 0
    for x in password:
        if (x in vowels):
            vowel_count+=1
    print ("tips: det finns "+str(vowel_count)+" vokaler i lösenordet")

