word = input("Enter a word: ")
latin_chars = "iao"
is_substituted = False

for char in word:
    if char in latin_chars:
        is_substituted = True
        break

if is_substituted:
    print("Substitution found: Yes")
else:
    print("Substitution found: No")