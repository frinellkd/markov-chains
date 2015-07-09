import sys
import random

text_source = sys.argv[1]


def make_chains(text_source):
    """Takes input text as string; returns dictionary of markov chains."""

    # Open the file at the file path provided
    open_file = open(text_source)

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

dictionary = make_chains(text_source)

def make_text(dictionary):
    """Takes dictionary of markov chains; returns random text."""

    

    # select a random word
    first_key = random.choice(dictionary.keys())
    
    # Start sentence with both words in first key
    goofy_sentence = first_key[0] + " " + first_key[1]

    
    # Run as long as key is in the dicitonary    
    while first_key in dictionary:

        # go back to dictionary, find values of the key that we returned
        # randomly select word from that list
        next_word = random.choice(dictionary[first_key])

        # add that randomly selected word to the sentence
        goofy_sentence += " " + next_word

        # find key that starts with the second value in first_word and the randomly selected
        # then assigns it to first key to continue loop
        # ex:
            # first_key ('Would', 'you')
            # next_word ('could')
            # --> first_key ('you', 'could')
        first_key = (first_key[1],next_word) 
        

    lower_goofy = goofy_sentence.lower()
    lower_goofy_cap = lower_goofy.capitalize()
    
    end_sent_punc = ["!", "." , "?"]
    punc_count_period = lower_goofy.count(".")
    punc_count_ques = lower_goofy.count("?")


    print lower_goofy_cap
    print end_sent_punc
    print punc_count_period
    print punc_count_ques
    


print make_text(dictionary)
