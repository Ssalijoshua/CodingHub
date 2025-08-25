# User should be prompted for input
message = input("Please enter your message:\n")

print("1. Caesar cipher\n")
print("2. Reverse cipher\n")
print("3. Vernam cipher\n")

encryption_algorithm = input("Enter the number of the encryption algorithm you want to use: ")

# ENCRYPT
# 1.Caesar Cipher
split_message = list(message)

k = input("To how many characters do you want to shift the characters: ")

ascii_message = [ord(x) for x in split_message]
print(ascii_message)

ascii_cypher = []

for x in ascii_message:
    y = x + int(k)
    ascii_cypher.append(y)

cypher = [chr(x) for x in ascii_cypher]

cypher_text = ''.join(cypher)
print(cypher_text)


# Decrypt

cypher = input("Enter the cyphertext to decrypt: ")
x = input("Enter the short value that was used to shift the cypher")

cypher_list = list(cypher)

cypher_list = [ord(a) for a in cypher_list]

message = []

for a in cypher_list:
    y = a - int(k)
    message.append(chr(str(y)))

''.join(message)

print(message)





