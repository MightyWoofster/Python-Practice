word = input("Enter phrase: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
newWord = word.lower()
for w in newWord:
	if w not in alphabet:
		newWord = newWord.replace(w, "")
most1 = 0
one = ""
most2 = 0
two = ""
most3 = 0
three = ""
for char in newWord:
	counts = newWord.count(char)
	if counts > most1:
		most1 = counts
		one = char
	elif counts > most2 and char != one:
		most2 = counts
		two = char
	elif counts > most3 and char != one:
		if char != two:
			most3 = counts
			three = char
print("Most often letter: " + one)
print("Second most often letter: " + two)
print("Third most often letter: " + three)

#extra credit portion
rotation1 = alphabet.index(one)-alphabet.index("e")
rotation2 = alphabet.index(two)-alphabet.index("e")
rotation3 = alphabet.index(three)-alphabet.index("e")
print("3 most likely Caesar rotations in order: " + str(rotation1) + ", " + str(rotation2) + ", " + str(rotation3))

ind = 0
decode1 = word
for char in decode1:
	if char in alphabet:
		index = alphabet.index(char)-rotation1
		if index<0:
			index += 26
		if index>25:
			index-=26
		newChar = alphabet[index]
		decode1 = decode1[: ind] + newChar + decode1[ind+1:]
	ind += 1
print("Most possible decoded text with rotation " + str(rotation1) + ": " + decode1)

ind = 0
decode2 = word
for char in decode2:
	if char in alphabet:
		index = alphabet.index(char)-rotation2
		if index<0:
			index += 26
		if index>25:
			index-=26
		newChar = alphabet[index]
		decode2 = decode2[: ind] + newChar + decode2[ind+1:]
	ind += 1
print("Second most possible decoded text with rotation " + str(rotation2) + ": " + decode2)

ind = 0
decode3 = word
for char in decode3:
	if char in alphabet:
		index = alphabet.index(char)-rotation3
		if index<0:
			index += 26
		if index>25:
			index-=26
		newChar = alphabet[index]
		decode3 = decode3[: ind] + newChar + decode3[ind+1:]
	ind += 1
print("Third most possible decoded text with rotation " + str(rotation3) + ": " + decode3)
	

