def find_shortest_word():
    data = input("Enter words separated by space: ")
    words = data.split()
    
    if words:
        shortest = min(words, key=len)
        print("Shortest word is:", shortest)
    else:
        print("The list is empty")

find_shortest_word()