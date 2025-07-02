Vigenère Cipher: String Manipulation Project
This project implements a Vigenère cipher, a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It's a classic example of polyalphabetic substitution, offering a significant improvement in security over single-alphabet ciphers.

Features
Encryption: Encrypts a given message using a custom keyword.

Decryption: Decrypts a Vigenère-encrypted message back to its original form using the same keyword.

Case-Insensitive (for processing): Converts input messages to lowercase for processing, maintaining non-alphabetic characters.

Handles Non-Alphabetic Characters: Preserves spaces, numbers, and symbols in the message during encryption and decryption.

How it Works (Vigenère Cipher)
The Vigenère cipher uses a keyword to determine the shift for each letter. Each letter of the keyword corresponds to a different Caesar cipher shift.

For encryption:

The message and key are converted to lowercase.

For each letter in the message:

If it's a letter, the corresponding letter from the key is used. The key is repeated as necessary to match the length of the message.

The offset is determined by the position of the key letter in the alphabet (e.g., 'a' is 0, 'b' is 1, etc.).

The index of the message letter in the alphabet is found.

The new_index for the encrypted letter is calculated as (index + offset) % 26 (where 26 is the length of the alphabet).

The letter at new_index in the alphabet is appended to the final_message.

Non-alphabetic characters are appended directly without modification.

For decryption, the process is similar, but the offset is subtracted instead of added: (index - offset) % 26.

Files
main.py (or your Python script name): Contains the implementation of the Vigenère cipher functions.

Usage
To use the cipher, you can directly run the main.py script (or whatever you named your file).

Functions
vigenere(message, key, direction=1):

The core function that performs both encryption and decryption.

message (str): The text to be encrypted or decrypted.

key (str): The keyword to use for the cipher.

direction (int): 1 for encryption (default), -1 for decryption.

Returns the processed message as a string.

encrypt(message, key):

A wrapper function for vigenere to perform encryption easily.

message (str): The text to encrypt.

key (str): The encryption keyword.

Returns the encrypted message.

decrypt(message, key):

A wrapper function for vigenere to perform decryption easily.

message (str): The text to decrypt.

key (str): The decryption keyword.

Returns the decrypted message.

Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: wearediscoveredsaveyourself