"""
Decryption Script - Advanced Encryption Tool
---------------------------------------------
A standalone Python script to decrypt encrypted files using the Fernet module from the cryptography library.

Developed by: Satya Upendra Samana
Internship: Codetech IT Solutions
"""

from cryptography.fernet import Fernet


def load_key():
    """
    Load the encryption key from the file 'encryption_key.key'.
    Returns:
        bytes: The encryption key.
    """
    try:
        with open("encryption_key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("[!] Error: 'encryption_key.key' not found. Please generate a key first.")
        exit()


def decrypt_file(input_file, output_file, key):
    """
    Decrypt an encrypted file and save the decrypted content to a new file.

    Args:
        input_file (str): Path of the encrypted file to decrypt.
        output_file (str): Path where the decrypted file will be saved.
        key (bytes): Encryption key used for decryption.
    """
    cipher = Fernet(key)

    try:
        with open(input_file, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        with open(output_file, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"[+] Decryption successful! File saved as: '{output_file}'")

    except FileNotFoundError:
        print(f"[!] Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"[!] Decryption failed: {e}")


if __name__ == "__main__":
    # Load the encryption key
    key = load_key()

    # Specify file paths (modify as needed)
    encrypted_file = "encrypted_data.enc"      # Replace with your actual encrypted file
    decrypted_file = "decrypted_output.txt"    # Desired output filename

    # Perform decryption
    decrypt_file(encrypted_file, decrypted_file, key)
