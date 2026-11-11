# 1. Find the Length of a Name
print("1. FIND THE LENGTH OF A NAME")

name = input("Enter your name: ")
print("Name:", name)
print("Length:", len(name))


# 2. Count Characters in a Sentence
print("\n2. COUNT CHARACTERS")

text = input("Enter a sentence: ")
print("Total characters:", len(text))


# 3. Convert Name into Uppercase
print("\n3. CONVERT INTO UPPERCASE")

name = input("Enter your name: ")
print("Uppercase:", name.upper())


# 4. Replace a Word
print("\n4. REPLACE A WORD")

text = "I love Java"
new_text = text.replace("Java", "Python")
print("Original:", text)
print("After replacement:", new_text)


# 5. Count Occurrences of a Character
print("\n5. COUNT A CHARACTER")

text = input("Enter a word: ")
ch = input("Enter a character: ")
print("Character count:", text.count(ch))

# 6.	Reverse a String
print(“\n6.	REVERSE A STRING”)

text = input(“Enter a word: “)
print(“Original:”, text)
print(“Reversed:”, text[::-1])


# 7.	Check Whether a Word is a Palindrome
print(“\n7.	PALINDROME CHECK”)

word = input(“Enter a word: “)

if word  word[::-1]:
    print(“Palindrome”)
else:
    print(“Not Palindrome”)