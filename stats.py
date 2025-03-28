
# Takes the entire text and splits it into individual words
def number_of_words(text):
    # text is defined in main as the entire book text at the specified file_path
    words = text.split()
    return len(words)

def number_of_char(text):
    chars = list(text.lower())
    count = {}
    # for unique characters in chars, if characters in char == unique characters, +1 to that unique character.
    for i in chars:
        if i.isalpha() == True: # checks to see if the character is part of the alphabet and not random characters i.e. a space ' '
            count[i] = count.get(i, 0) + 1
    
    return count



