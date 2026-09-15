def add_two_numbers() -> int:
    line = input()
    num = line.split(",")
    int_list = []
    
    for n in num:
        int_list.append(int(n))

    return int_list[0] + int_list[1]
    
# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
