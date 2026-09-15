from typing import List

def read_integers() -> List[int]:
    num_list = []
    numbers = input()
    num_list = numbers.split(",")
    new_list = list(map(int, num_list))
    return new_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
