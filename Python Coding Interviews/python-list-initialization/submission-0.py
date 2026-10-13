from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    mylist = [0] * (size - 1)

    for i in range(size):
        if index == i:
            mylist.insert(i, value)

    return mylist


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
