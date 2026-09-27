from typing import List

# def getWordLength(word: str) -> int:
#     return len(word)


def sort_words(words: List[str]) -> List[str]:
    for i in range(len(words)):
        for j in range(len(words) - 1):
            if len(words[j+1]) > len(words[j]):
                words[j], words[j+1] = words[j+1], words[j]
    return words
                


def sort_numbers(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)): # number of passes
        for j in range(len(numbers) - 1): # 2 sliding window
            if abs(numbers[j]) > abs(numbers[j+1]): # comparison
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] # current = next, next = current
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
