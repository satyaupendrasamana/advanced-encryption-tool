from cryptography.fernet import Fernet

# Generate and save the encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as 'encryption_key.key'")

# Load the existing encryption key
def load_key():
    return open("encryption_key.key", "rb").read()

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_path + ".encrypted", "wb") as enc_file:
        enc_file.write(encrypted_data)
    
    print(f"File '{file_path}' successfully encrypted as '{file_path}.encrypted'")

# Decrypt a file
def decrypt_file(encrypted_file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(encrypted_file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    original_file_path = encrypted_file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"File '{encrypted_file_path}' successfully decrypted as '{original_file_path}'")

# Main menu
def main():
    print("Choose an option:")
    print("1. Generate Encryption Key")
    print("2. Encrypt a File")
    print("3. Decrypt a File")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        generate_key()
    elif choice == '2':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path)
    elif choice == '3':
        encrypted_file_path = input("Enter the path of the file to decrypt: ")
        decrypt_file(encrypted_file_path)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()