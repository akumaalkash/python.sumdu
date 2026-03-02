sentence = input("Enter a sentence: ")
result = ""

for char in sentence:
    result += str(ord(char)) + " "

print("ASCII sentence is:", result.strip())