def count_words(text):
    words = text.split()
    return len(words)

# Example usage:
text = input("Enter some text : ")
word_count = count_words(text)
print(f"The text contains {word_count} words.")

input("Press Enter to close...")