# User should be prompted for input
message = input("Please enter your message:\n")


print("1. Caesar cipher\n")
print("2. Reverse cipher\n")
print("3. Vernam cipher\n")

encryption_algorithm = input("Enter the number of the encryption algorithm you want to use: ")

# ENCRYPT
# 1.Caesar Cipher
split_message = list(message)
print(split_message)

k = input("To how many characters do you want to shift the characters: ")

ascii_message = [ord(x) for x in split_message]





# Decrypt

