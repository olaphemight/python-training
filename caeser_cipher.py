
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x", "y", "z", " ", "@", "&", "^", "#", "*", ",", "$", ".", "-", ".", "/", "?", ">", "<", "!",
"|", "=", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x", "y", "z"]



# def encrypt(plain_text, shift_amount):
#     cipher_code = ""
    
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_code +=new_letter
#     print(f'The encoded text is {cipher_code}')


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)


# if direction == "decode":
#         encrypt(plain_text=text, shift_amount= -shift)

        # def decrypt(plain_text, shift_amount):
#     cipher_code = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_code += new_letter
#     print(f'The decrypted text is {cipher_code}')

# decrypt(plain_text=text, shift_amount=shift)


# Adding some characters to the code

# def caeser(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             if cipher_direction == "encode":
#                 new_position = position + shift_amount
#             elif cipher_direction == "decode":
#                 new_position = position - shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f'The {cipher_direction}d text is: {end_text}')







# Final code, all in a function

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
        elif cipher_direction == "decode":
            new_position = position - shift_amount
        
        end_text += alphabet[new_position]
         
    print(f'The {cipher_direction}d text is: {end_text}')




should_continue = True

while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
        text = input("Type your message:\n ").lower()
        shift = int(input("Type your shift number:\n"))
        # print(shift)
        shift = shift % 25
        # print(shift)
        caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

        result = input("Type 'yes' to continue, 'No' to stop: ").lower()
        if result == "no":
                should_continue = False
        print("Goodbye")
        






