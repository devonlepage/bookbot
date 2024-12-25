# TODO: Sort character counts

# Integer Dict -> Void
def print_report(file, num_words, character_count):
    # Header
    print(f"--- Begin report of {file} ---")
    
    # Word count
    print(f"{num_words} found in the document\n")
    
    # Sorted character counts:
    for ch in character_count:
        print(f"The '{ch}' character was found {character_count[ch]} times")
        
    # Footer
    print(f"--- End report ---")

def main():
    frankenstein = 'books/frankenstein.txt'
    with open(frankenstein) as f:
        file_contents = f.read()

        ## PRINTING FILE CONTENTS
        # print(file_contents)
        
        word_count = len(file_contents.split())

        ## COUNTING CHARACTERS
        # a list containing the lowercase letters 'a' thru 'z'
        letters = list('abcdefghijklmnopqrstuvwxyz')

        # a dictionary whose keys are the letters 'a' thru 'z', initialized to 0
        characters = {}
        for let in letters:
            characters[let] = 0
        
        for ch in file_contents.lower():
            if ch in characters:
                characters[ch] += 1 

        print_report(frankenstein, word_count, characters)

main()