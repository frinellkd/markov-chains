import sys


def make_chains(filepath):
    """Takes input text as string; returns dictionary of markov chains."""

    # Open the file at the file path provided
    open_file = open(filepath)

    # Reads the files and returns the file text as one long string
    body_string = open_file.read()

    # splits the text string on whitespace removing tabs, new lines, etc.
    word_list = body_string.split()

    # assigns an empty dictionary to markov_pairs
    markov_pairs = {}

    # Traversing through indices until we reach the second-to-last word.
    # Stop at 2 because the last word will never need to be a key.
    for i in range(len(word_list) - 2):

        # Creates a new tuple where first item is a word, and second item is 
        # the word that comes after
        pair = word_list[i], word_list[i+1]

        if pair in markov_pairs:

            # Adding the word after the pair [i+2] as a value 
            markov_pairs[pair].append(word_list[i+2])
        
        else:
            # If pair is not in markov_pairs, add key and value
            # where value is a list containing word immediately after pair [i+2]
            markov_pairs[pair] = [word_list[i+2]]    
        
    # for keys, value in markov_pairs.items():
    #     print keys, value

    return markov_pairs

make_chains("green-eggs.txt")

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
