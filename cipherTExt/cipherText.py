# caesar cipher is also encrption technique.
plain_txt = "Hello, World!"
shift = 3
def caser_cipher(text, shift, encrypt=True):
    shift = shift if encrypt else -shift

    def shift_char(char):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            return chr((ord(char)-base+shift) % 26+base)
        else:
            return char
    return ''.join([shift_char(char) for char in text])
encrypt_text = caser_cipher(text=plain_txt, shift=shift, encrypt=True)
print(f" encrypt_text -> {encrypt_text} . ")
decrypt_text = caser_cipher(text=encrypt_text, shift=shift, encrypt=False)
print(f" decrypt_text -> {decrypt_text} . ")
