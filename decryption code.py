from cryptography.fernet import Fernet

# Function to load the encryption key
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Function to decrypt a file
def decrypt_file(input_file, output_file, key):
    cipher = Fernet(key)

    with open(input_file, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Decryption successful! Decrypted file saved as: {output_file}")

# Load the encryption key
key = load_key()

# Specify the encrypted file and output file
encrypted_file = "encrypted_data.enc"  # Change this to the actual encrypted file name
decrypted_file = "decrypted_output.txt"  # Change this to the desired output file name

# Perform decryption
decrypt_file(encrypted_file, decrypted_file, key)
