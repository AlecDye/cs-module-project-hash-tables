"""
input: Hello, my cat. And my cat doesn't say "hello" back.

output: {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}

output keys must be lower case

ignore these characters: " : ; , . - + = / \ | [ ] { } ( ) * ^ &

"""


def word_count(s):
    # Your code here
    cache = {}
    trash = [
        '"',
        ":",
        ";",
        ",",
        ".",
        "-",
        "+",
        "/",
        "|",
        "[",
        "]",
        "{",
        "}",
        "(",
        ")",
        "*",
        "^",
        "&",
        "\\",
    ]
    # convert string input to lowercase
    res = s.lower()

    for i in trash:
        res = res.replace(i, "")

    res = res.split()

    # should have none of the unwanted values
    for u in res:
        if u in cache:
            count = cache[u]
            count += 1
            cache[u] = count
        else:
            cache[u] = 1

    # print(cache)
    return cache
    # returns None None None None


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )

