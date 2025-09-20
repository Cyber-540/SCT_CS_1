# SCT_CS_1
Program Description

This Python program implements a Caesar Cipher, one of the simplest and oldest encryption techniques. The Caesar Cipher works by shifting each letter in the message by a fixed number of positions in the alphabet.

The program allows the user to both encrypt and decrypt messages by specifying the mode and a shift value.

How It Works

Function caesar_cipher(text, shift, mode)

Takes three inputs:

text → the message to encrypt or decrypt

shift → the number of positions each letter should be shifted

mode → whether the operation is "encrypt" or "decrypt"

If the mode is "decrypt", the shift value is made negative to reverse the direction of shifting.

It loops through each character of the message:

If it’s a letter (A–Z or a–z), the program shifts it within the alphabet while preserving case.

Non-alphabet characters (like spaces, numbers, or punctuation) are kept unchanged.

The modified text is built and returned.

Main Program

Asks the user to input:

A message

A shift value (integer)

A mode (encrypt or decrypt)

Calls the caesar_cipher function with these inputs.

Prints the resulting encrypted or decrypted message.
