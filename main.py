from stats import number_of_words, number_of_char
import sys

def main(): # no need to fill 'main' with a 

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    # captures the the entire text of the book in 'text'
    text = get_book_text(file_path)

    # captures the number of words inside the book in 'word_count'
    word_count = number_of_words(text)

    char_count = number_of_char(text)
    sorted_char_count = dict(sorted(char_count.items(), key =lambda item: item[1], reverse= True))

    # prints the number of words inside the text document
    # print(f"{word_count} words found in the document \n {char_count}")

    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in sorted_char_count.items():
        print(f"{key}: {value}")
    print("============= END ===============")

def get_book_text(file_path):
    # file_path is defined in main as the path to the book
    with open(file_path) as f:
        return f.read()
    
# Takes the entire text and splits it into individual words (now imported from 'stats.py' in the same folder)
# def number_of_words(text):
#    # text is defined in main as the entire book text at the specified file_path
#    words = text.split()
#    return len(words)

main()

# I define a function called 'get_book_text' that takes a file path as input and returns the text of the book as a string.
# then i call 'main()' that uses 'get_book_text' function. Thus, the file_path needs to be in 'main' so that it can be used by 'get_book_text' function.
# The file_path is '/Users/danielbazan/Desktop/SandBox/bootdev/bookbot/books/frankenstein.txt' which is the path to the book 'Frankenstein' in the 'books' directory.
# The 'main' function calls 'get_book_text' with the file_path as an argument and prints the text of the book to the console.
# The text of the book is then printed to the console.