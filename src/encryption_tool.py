"""
Advanced Encryption Tool
-------------------------
A Python-based script for encrypting and decrypting files using AES-256 encryption through the Fernet module from the cryptography library.

Developed by: Satya Upendra Samana
Internship: Codetech IT Solutions
"""

from cryptography.fernet import Fernet


def generate_key():
    """
    Generate a secure encryption key and save it to 'encryption_key.key'.
    """
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Encryption key generated and saved as 'encryption_key.key'.")


def load_key():
    """
    Load the existing encryption key from the file.
    """
    try:
        with open("encryption_key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("[!] Error: Encryption key file not found. Please generate a key first.")
        exit()


def encrypt_file(file_path):
    """
    Encrypt a specified file using the encryption key.
    """
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_path + ".encrypted", "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"[+] File '{file_path}' encrypted successfully as '{file_path}.encrypted'.")


def decrypt_file(encrypted_file_path):
    """
    Decrypt an encrypted file using the encryption key.
    """
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_file_path = encrypted_file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"[+] File '{encrypted_file_path}' decrypted successfully as '{original_file_path}'.")


def main():
    """
    Display a menu to perform key generation, encryption, or decryption.
    """
    print("\n=== Advanced Encryption Tool ===")
    print("1. Generate Encryption Key")
    print("2. Encrypt a File")
    print("3. Decrypt a File")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == '1':
        generate_key()
    elif choice == '2':
        file_path = input("Enter the path of the file to encrypt: ").strip()
        encrypt_file(file_path)
    elif choice == '3':
        encrypted_file_path = input("Enter the path of the file to decrypt: ").strip()
        decrypt_file(encrypted_file_path)
    else:
        print("[!] Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
