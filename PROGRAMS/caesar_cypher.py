#A python program to illustrate the Caesar Cipher encryption

def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result



#take inputs for the function
text = input("Enter text for encryption:")
s = int(input("Shift:"))

#output the result
print("Cipher: " + encrypt(text,s))

#wait for user to finish
input()

