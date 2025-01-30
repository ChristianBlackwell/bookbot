def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Get word count
    word_count = count_words(file_contents)
    
    # Get character count and convert to sorted list
    char_counts = count_characters(file_contents)
    char_list = convert_dict_to_list(char_counts)
    
    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    # Print each character count
    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    
    print("--- End report ---")

def count_words(sentence):
    word_count = len(sentence.split())
    return word_count

def count_characters(string):
    characters_used = {}
    lowered_string = string.lower()

    for character in lowered_string:
        if character not in characters_used:
            characters_used[character] = 1  # First time we see this character
        else:
            characters_used[character] += 1  # We've seen this character before
    return characters_used

def sort_on(dict):
    return dict["num"]  #This helper function tells sort() which value to use
        
def convert_dict_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():

        #create a dictionary for each character
        if char.isalpha():
            char_info = {"char": char, "num": count}
            char_list.append(char_info)

    #sort the list be frequency (highest to lowest)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    



main() #This goes at the bottom, to ensure everything is defined before being called.