ciphertext = input("Enter ciphertext :> ")                                      # takes ciphertext input from user
ciphertext = ciphertext.upper()                                                 # conversts ciphertext input into an uppercase form to prevent any syntax errors

unsolved = list(ciphertext)                                                     # converting ciphertext string into a list
unicodeUnsolved = []                                                            # lines 5 - 6 making empty lists to dump info in
unicodeSolved = []
count = -1                                                                      # counter

for i in range (0,len(unsolved)):                                               # converting ciphertext list into their ASCII values and then dumping them into a list
    unicodeUnsolved.append(int(ord(unsolved[i])))

with open ("dump.txt", "w") as file:                                            # opening dump.txt file to dump every possible shift in
    for j in range (0,26):                                                      # looping 26 times, for the 26 shifts that could be done.
        count += 1                                                              # increasing counter by one
        unicodeSolved = []                                                      # reseting the solved list
        for k in range (len(unsolved)):                                         # looping for the length of the ciphertext sent.
            unicodeSolved.append(unicodeUnsolved[k] + count)                    # adding the count to the ASCII value of the ciphertext to simulate the shift, and then put it into the solved list
            if (unicodeSolved[k] - count) != 32:                                # checking if the value is not a space
                if unicodeSolved[k] > 90:                                       # if the shift goes above the upper bound of the ASCII values of uppercase letters... 
                    unicodeSolved[k] = int(unicodeSolved[k]) - 26               # ... the ASCII value gets subtracted by 26 to bring it back to the start of the alphabet.
                unicodeSolved[k] = chr(unicodeSolved[k])                        # converting the ASCII value back into a character.
            else:                                                               
                unicodeSolved[k] = " "                                          # if the value was a space, then a space is inputted.
            file.write(unicodeSolved[k])                                        # writing the values of the shifts into the dump.txt file
        file.write("\n")                                                        # adding a new line after every successful shift to prevent confusion when viewing the dump file.