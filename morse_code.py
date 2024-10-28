'''

Morse code, also known as American or Railroad Morse code, was developed by Samuel F. B. Morse
in the United States during the 1830s to represent letters of the alphabet, numerals, and punctuation
for electric telegraphy using an arrangement of dots and dashes. The original Morse code was further 
improved by Alfred Lewis Vail, Morse's assistant and partner. Later use of Morse code in Europe identified 
that it was insufficient to support non-English text like diacritical marks. This led to the development of 
International Morse Code, or Continental Morse Code as it is now known, in 1951.

The most famous Morse code sequence is probably the one for SOS (Save Our Souls), denoted dot-dot-dot, 
dash-dash-dash, dot-dot-dot. This is because dot-dot-dot represents S, and dash-dash-dash represents O
in Morse code.

Create a program to decode a message into Morse code. Morse code uses a sequence of dots and dashes to 
encode letters, numbers, and the space character. The table below shows the conversion from American Morse 
code to individual characters. A single space separates the dot–dash pattern for each character. Three spaces 
represent a space character. You can use period for dot and hyphen for dash in your program.

Psuedocode: 


    Build a data structure to hold the letter-number to dot-dash conversions.
    Ask the user to enter a sentence.
    Convert the sentence to uppercase.
    Use your data structure to convert each letter, number, and space to its equivalent dot-dash pattern. You can ignore anything that's not a letter, number, or space.
    Print the conversion for the user.
    Ask the user if they want to enter another sentence. Based on this, accept another sentence for conversion or quit the program. 

'''
import pandas as pd 

dict_code = {
"A": ".-",
"B": "-...",
"C": "-.-.",
"D": "-..",
"E": ".",
"F": "..-.",
"G": "--.",
"H": "....",
"I": "..",
"J": ".---",
"K": "-.-",
"L": ".-..",
"M": "--",
"N": "-.",
"O": "---",
"P": ".--.",
"Q": "--.-",
"R": ".-.",
"S": "...",
"T": "-",
"U": "..-",
"V": "...-",
"W": ".--",
"X": "-..-",
"Y": "-.--",
"Z": "--..",
" ": " ",
"1": ".----",
"2": "..---",
"3": "...--",
"4": "....-",
"5": ".....",
"6": "-....",
"7": "--...",
"8": "---..",
"9": "----.",
"0": "-----"
}



store = []
playing = True

while playing == True: 
    sentence = input("Please enter a sentence: ").upper()
    for i in sentence: 
        store.append(dict_code[i])  

    print(*store)

    new_sentence = input("Do you want to enter a new sentence? (Yes/No) ")

    if new_sentence == "Yes": 
        continue
    else: 
        break


