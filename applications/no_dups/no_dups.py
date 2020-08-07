"""
Input: a string of words separated by spaces. Only the letters `a`-`z`
are utilized.

Output: the string in the same order, but with subsequent duplicate
words removed.

"""

cache = {}


final = []


def no_dups(s):
    # split string
    if len(s) < 1:
        return ""
    for word in s.split():
        # put words into cache if they aren't already there
        if word not in cache:
            cache[word] = 1
            final.append(word)
    return " ".join(final)


# print(no_dups("cats dogs fish cats dogs"))

# if __name__ == "__main__":
print(no_dups(""))
print(no_dups("hello"))
print(no_dups("hello hello"))
print(no_dups("cats dogs fish cats dogs"))
print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
