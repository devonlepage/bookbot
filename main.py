# String -> Dict
# given a string representing a document, return a dict containing counts of the characters
#  'a' through 'z'
def count_characters(document):
    # list of the lowercase letters 'a' thru 'z'
    letters = list('abcdefghijklmnopqrstuvwxyz')

    # a dictionary whose keys are the letters 'a' thru 'z', initialized to 0
    characters = {}
    for let in letters:
        characters[let] = 0
    
    # iterate through the document and tally the letters found
    for ch in document.lower():
        if ch in characters:
            characters[ch] += 1

    return characters
                
# Dict -> Dict
# given a Dict containing k-v pairs representing character counts (e.g., 'a': 10),
#  produces a Dict with k-v pairs ordered by frequency
def sort_characters(characters):
    table = []
    
    for ch in characters:
        cnt = characters[ch]
        row = {'char': ch, 'count': cnt}
        table.append(row)
    
    # Dict -> Integer
    # given a dict representing a character count, return the 'count' value
    def get_count(row):
        return row['count']
    
    table.sort(key=get_count, reverse=True)
    tmp = {}
    for row in table:
        ch = row['char']
        cnt = row['count']
        tmp[ch] = cnt

    return tmp

# String Integer Dict -> Void
# prints a report of a given file with word and character counts
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
        
        ## COUNTING WORDS
        word_count = len(file_contents.split())

        ## COUNTING CHARACTERS
        characters = count_characters(file_contents)

        print_report(frankenstein, word_count, sort_characters(characters))

main()