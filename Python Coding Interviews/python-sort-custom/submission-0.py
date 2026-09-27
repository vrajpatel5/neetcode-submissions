from typing import List

def getWordLength(word: str) -> int:
    return len(word)


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=getWordLength, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if abs(numbers[j]) > abs(numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
