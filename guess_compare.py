from utils.constants import PASSWORD_LENGTH
 # returnernar en "******" sträng som visar korrekta bokstäver samt en lista med karaktärer som finns i ordet men är på fel plats
def guess_compare(user_input, bot_password, known_password, contained_characters):
    
    for x in range(PASSWORD_LENGTH):
        if (user_input[x] in bot_password):
            if (user_input[x] == bot_password[x]):
                if (known_password[x] != user_input[x]): #ser till så att man inte ändrar på strängen i onödan (att man redan fått rätt förr)
                    known_password = update_known_password(known_password, x, user_input[x])
                    print('Tecknet ' + user_input[x]+ " var på rätt plats!")
                if (user_input[x] in contained_characters):
                    contained_characters.remove(user_input[x])
                continue
            else:
                print('Tecknet (' + user_input[x] + ") finns i lösenordet men var inte på rätt plats")
                if (user_input[x] not in contained_characters and user_input[x] not in known_password):
                    contained_characters.append(user_input[x])
    return (known_password, contained_characters)
#liten kommentar angående rätt-meddelanden, kan ev. göra så att allt skrivs på en gång istället för flera rader av "x finns i ordet men..."

#använer pythons "slicing" för att ta isär strängen och stoppa in rätt karaktär ('x')
def update_known_password(known_password, index, x):
    temp = known_password[:index]
    temp2 = known_password[index+1:]
    # print (temp + "  ,  " + temp2) - var bara ett test för att se ifall det funkar

    return temp + x + temp2

