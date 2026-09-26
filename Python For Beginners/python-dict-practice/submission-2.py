from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    cDict = {}
    for letter in word:
        counter = 1
        if letter in cDict:
            cDict[letter] += 1
        else:
            cDict[letter] = 1
    return cDict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
