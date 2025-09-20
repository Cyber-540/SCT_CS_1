def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift  # reverse shift for decryption

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


# Main program
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

output = caesar_cipher(message, shift, mode)
print(f"{mode.capitalize()}ed message:", output)
