#!/usr/bin/env python3
from caesar_util import is_word_english

__author__ = "Steven Yulong Yan"

MIN_OFFSET = 1
MAX_OFFSET = 25


def get_option():
    """
    Return the option the user inputs.
    :return: (str) One of the four letters, namely e, d, a and q.
    """
    while True:
        input_option = input("Please choose an option [e/d/a/q]:\n"
                             "  e) Encrypt some text\n"
                             "  d) Decrypt some text\n"
                             "  a) Automatically decrypt English text\n"
                             "  q) Quit\n> ")
        if input_option in "e d a q".split():
            return input_option
        else:
            print("Invalid command\n")


def get_text(input_option):
    """
    Return the text the user inputs.
    :param input_option: (str) One of the four letters, namely e, d, a and q.
    :return: (str) The text the user inputs.
    """
    global input_text
    if input_option == "e":
        input_text = input("Please enter some text to encrypt: ")
    elif input_option == "d":
        input_text = input("Please enter some text to decrypt: ")
    elif input_option == "a":
        input_text = input("Please enter some encrypted text: ")
    elif input_option == "q":
        input_text = None
    return input_text


def get_offset(option):
    """
    Return the offset the user inputs.
    :param option: (str) One of the four letters, namely e, d, a and q.
    :return: (int) One of the numbers from 0 to 25.
    """
    while option != "a":
        input_offset = input("Please enter a shift offset (1-25): ")  # 0 is allowed.
        try:
            offset = int(input_offset)
            if MIN_OFFSET - 1 <= offset <= MAX_OFFSET:
                return offset
            else:
                print("The integer is out of range. Please try again.\n")
        except ValueError:
            print("The entry can only be an integer. Sorry...\n")


def encrypt(text, offset):
    """
    Return the encrypted text by using the corresponding ASCII codes as carriers.
    :param text: (str) The text the user inputs.
    :param offset: (int) the offset the user inputs.
    :return: (str) The encrypted text.
    """
    encrypted = ""
    for character in text:
        if character.isalpha():
            decimal = ord(character)
            decimal += offset
            if character.isupper():
                if decimal > ord("Z"):  # Ensures the number remains in the designated range.
                    decimal -= 26
            elif character.islower():
                if decimal > ord("z"):  # Ensures the number remains in the designated range.
                    decimal -= 26
            encrypted += chr(decimal)
        else:
            encrypted += character
    return encrypted


def decrypt(text, offset):
    """
    Return the decrypted text by using the corresponding ASCII codes as carriers.
    :param text: (str) The text the user inputs.
    :param offset: (int) the offset the user inputs.
    :return: (str) The decrypted text.
    """
    decrypted = ""
    for character in text:
        if character.isalpha():
            decimal = ord(character)
            decimal -= offset  # Decryption is essentially the reverse engineering of encryption.
            if character.isupper():
                if decimal < ord("A"):  # Ensures the number remains in the designated range.
                    decimal += 26
            elif character.islower():
                if decimal < ord("a"):  # Ensures the number remains in the designated range.
                    decimal += 26
            decrypted += chr(decimal)
        else:
            decrypted += character
    return decrypted


def find_encryption_offsets(encrypted_text):
    """
    Return the offset by which successfully decrypt the encrypted text into plain English.
    :param encrypted_text: (str) The encrypted text the user inputs.
    :return: (tuple) A tuple that contains all the applicable offsets stored as integers.
    """
    offsets = ()
    for offset in range(MIN_OFFSET, MAX_OFFSET + 1):
        decrypted_text = decrypt(encrypted_text, offset)
        decrypted_replaced = ""
        for character in decrypted_text:
            character_replaced = character.replace("-", " ")  # Replace all hyphens with white space.
            decrypted_replaced += character_replaced
        decrypted_removed = ""
        for character in decrypted_replaced:
            if character.isalpha() or character == " ":  # Check if a character is either a letter or an empty space.
                decrypted_removed += character
        decrypted_lower = decrypted_removed.lower()
        decrypted_split = decrypted_lower.split()
        if all(is_word_english(word) for word in decrypted_split):  # Ensures all words in a decryption are English.
            offsets += (offset,)
    return offsets


def tool(option, text, offset):
    """
    Output the result according to the option the user selects.
    :param option: (str) One of the four letters, namely e, d, a and q.
    :param text: (str) The text the user inputs.
    :param offset: (int) the offset the user inputs.
    """
    if option == "e":
        if offset == 0:
            print("The encrypted text is:")
            for offset in range(MIN_OFFSET, MAX_OFFSET + 1):  # Flush out all the encryption.
                print("  {:02}:".format(offset), encrypt(text, offset))
        else:
            encrypted_text = encrypt(text, offset)
            print("The encrypted text is: {}".format(encrypted_text))
    elif option == "d":
        if offset == 0:
            print("The decrypted text is:")
            for offset in range(MIN_OFFSET, MAX_OFFSET + 1):  # Flush out all the decryption.
                print("{:02}:".format(offset), decrypt(text, offset))
        else:
            decrypted_text = decrypt(text, offset)
            print("The decrypted text is: {}".format(decrypted_text))
    elif option == "a":
        key_offset = find_encryption_offsets(text)
        if len(key_offset) == 0:
            print("No valid encryption offset")
        elif len(key_offset) == 1:
            print("Encryption offset: {}".format(key_offset[0]))
            print("Decrypted message: {}".format(decrypt(text, key_offset[0])))
        else:
            keys_offset = ", ".join(str(offset) for offset in key_offset)  # Essentially converts a tuple to a string.
            print("Multiple encryption offsets: {}".format(keys_offset))


def main():
    """
    Implement the tool until the user chooses to quit.
    """
    print("Welcome to the simple encryption tool!\n")
    option = get_option()
    while option != "q":
        text = get_text(option)
        offset = get_offset(option)
        tool(option, text, offset)
        print()
        option = get_option()
    print("Bye!")


if __name__ == '__main__':
    main()
