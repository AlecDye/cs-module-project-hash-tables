import random

# UPER
## Understand

## Plan - we're done if we have good pseudocode
# 1. Read the file 'input.txt' and split it into words
### already read in
### split into words

# 2. Analyze the text, building up the dataset of which words can follow
### Which words can follow a word? any word that actually does
#### any word at index + 1
### How to build dataset?

### Use a hashtable
#### good way to relate one piece of info, with other info. relational
#### Frequent lookups
### Key: word, value: list of all the words that can follow this word

# 3. Choose a random "start word" to begin.
## What is a "start word"?
## First or second character is capitalized

## Make a list of start words

# 4. Loop through
## What's a stop word?
## Ends with .?!, or second-to-last character is

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# split into words
split_words = words.split()

# TODO: analyze which words can follow other words
dataset = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in dataset:
        dataset[word] = [next_word]

    else:
        dataset[word].append(next_word)

# Make a list of start words
## If first/second character is capitalized, put into list
## Loop over our split_words and put any start word into a list
start_words = []
for key in dataset.keys():
    if key[0].isupper() or len(key) > 1 and k[1].isupper():
        start_words.append(key)

word = random.choice(start_words)


## You can add a .keys() to your hashtable class (alternatively)


# TODO: construct 5 random sentences
# Your code here

stopped = False

stop_signs = "?.!"

while not stopped:
    # print the word
    print(word)

    ## if it's a stop word, stop
    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True

    # choose a random following word
    following_words = dataset[word]

    word = random.choice(following_words)
