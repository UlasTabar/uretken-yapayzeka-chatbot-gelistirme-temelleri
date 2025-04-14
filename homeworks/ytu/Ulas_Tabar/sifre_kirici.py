import string
import re

def encrypt_message(plain_text):

    encrypted_text = ""
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shift = 5


    parts = re.split('(\d+)', plain_text)

    for part in parts:
        if part.isdigit():

            encrypted_text += part[::-1]
        else:

            for char in part:
                if char in alphabet_lower:
                    original_pos = alphabet_lower.find(char)
                    new_pos = (original_pos + shift) % 26
                    encrypted_text += alphabet_lower[new_pos]
                elif char in alphabet_upper:
                    original_pos = alphabet_upper.find(char)
                    new_pos = (original_pos + shift) % 26
                    encrypted_text += alphabet_upper[new_pos]
                else:

                    encrypted_text += char
    return encrypted_text

def decrypt_message(encrypted_text):

    decrypted_text = ""
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shift = 5


    parts = re.split('(\d+)', encrypted_text)

    for part in parts:
        if part.isdigit():

            decrypted_text += part[::-1]
        else:

            for char in part:
                if char in alphabet_lower:
                    original_pos = alphabet_lower.find(char)
                    new_pos = (original_pos - shift + 26) % 26
                    decrypted_text += alphabet_lower[new_pos]
                elif char in alphabet_upper:
                    original_pos = alphabet_upper.find(char)
                    new_pos = (original_pos - shift + 26) % 26
                    decrypted_text += alphabet_upper[new_pos]
                else:

                    decrypted_text += char
    return decrypted_text


print("--- Şifreleme Programı ---")

while True:
    print("\nNe yapmak istersiniz?")
    print("1: Mesaj Şifrele")
    print("2: Mesaj Çöz")
    print("3: Programdan Çıkış")
    choice = input("Seçiminiz (1/2/3): ")

    if choice == '1':
        message = input("Şifrelenecek mesajı girin: ")
        encrypted = encrypt_message(message)
        print(f"\nŞifrelenmiş Mesaj: {encrypted}")
    elif choice == '2':
        message = input("Çözülecek mesajı girin: ")
        decrypted = decrypt_message(message)
        print(f"\nÇözülmüş Mesaj: {decrypted}")
    elif choice == '3':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

