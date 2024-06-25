import ceaser_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(ceaser_cipher_art.art)


def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "encode":
        for letter in text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                new_position = (alphabet.index(letter) + shift) % len(alphabet)
                cipher_text += alphabet[new_position]

    if direction == "decode":
        for letter in text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                new_position = (alphabet.index(letter) - shift) % len(alphabet)
                cipher_text += alphabet[new_position]
    print(f"Here is the {direction}d result: {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type encode to encrypt, type decode to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    repeat = input("Do you want to try again? yes/no\n")
    if repeat == "no":
        should_continue = False
