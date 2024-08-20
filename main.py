def count_words(file_contents):
    """Count the number of words in the given text."""
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    """Count the occurrences of each character in the given text."""
    file_contents = file_contents.lower()
    char_count = {}
    
    for char in file_contents:
        if char.isalpha():  # Count only alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def generate_report(file_contents):
    """Generate a formatted report of word and character counts."""
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    
    # Convert character count dictionary to a sorted list of dictionaries
    sorted_char_counts = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # Print the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print(f"--- End report ---")

def main():
    # Specify the relative path to the file
    path_to_file = "books/frankenstein.txt"
    
    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    # Generate and print the report
    generate_report(file_contents)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
