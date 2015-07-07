import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    body_text = open(corpus)

    body_string = ""
    
    for line in body_text:
        # concatenate all the lines together  
        line = line.rstrip()
        body_string = body_string + line + " "

    word_list = body_string.split(" ")

    markov_pairs = {}

    for i in range(len(word_list) - 1):
        pair = word_list[i], word_list[i+1]
        markov_pairs[pair] = None

    print markov_pairs

print make_chains("green-eggs.txt")

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
