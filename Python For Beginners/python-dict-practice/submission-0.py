from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    ccdict = {}
    for letter in word:
        if letter in ccdict:
            ccdict[letter] += 1
        else:
            ccdict[letter] = 1
    return ccdict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
