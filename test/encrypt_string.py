import simplyencrypt as en

keys = en.new_random_password(1024)
line = "Let's encrypt this line"
print("Unenceypted line: " + line)

cipher_text = en.encrypt(keys, line)
try:
	print("Encrypted line: " + str(cipher_text))
except:
	print("Encrypted: ", end=" ")
	for c in cipher_text:
		c = str(ord(c))
		print(c, end=", ")
	print("\n\nPrinted Encrypted line in termes of ord values cause the \
values couldn't be printed as utf-8 chars")
