logo = """           
                                    _       _               
                                   (_)     | |              
  ___ __ _  ___  ___  __ _ _ __ ___ _ _ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__/ __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \ (_| | | | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\__,_|_|  \___|_| .__/|_| |_|\___|_|   
                                     | |                    
                                     |_|                   
"""

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar():
    def encrypt(original_text, shift_amount):
        encoded_text = ""
        for letter in original_text:
            if letter not in alphabet:
                encoded_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                encoded_text += alphabet[shifted_position]
        print(f"\nHere is the encoded result: {encoded_text}\n")

    def decrypt(original_text, shift_amount):
        decoded_text = ""
        for letter in original_text:
            if letter not in alphabet:
                decoded_text += letter
            else:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                decoded_text += alphabet[shifted_position]
        print(f"\nHere is the decoded result: {decoded_text}\n")

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

loop = True

while loop:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
            print("Invalid Input.")
            break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar()
    
    continu_or_not = input("Do you want to continue encoding or decoding the messages?(yes/no):\n").lower()
    if continu_or_not == "yes":
        continue
    elif continu_or_not == "no":
        loop = False
    else:
        print("Invalid Input")
        break
    