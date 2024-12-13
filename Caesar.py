message = input('Input your message, and we will cipher and send it to her Majesty Queen Mary of Scots\n').upper()

alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

counter=0
caesar_cypher=""

for i in range(0, len(message)):

    for j in range(0, len(alphabet)):


        if message[i]==alphabet[j]:
            caesar_cypher+=alphabet[j+1]
            break
        elif message[i]=="Z":
            caesar_cypher+="A"
            break
        elif j==25:                         #need to print non-letter entries
            caesar_cypher+=message[i]
            break
        else:
               
            continue



print(caesar_cypher)
