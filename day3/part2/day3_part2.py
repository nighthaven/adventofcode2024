with open('./day3/input.txt', 'r') as file:
    lines = file.readlines()

list_input = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
string_lines = str(lines)

import re

def repair_all_mul(list_mul):
    result = 0
    to_multiply = []
    input_list = re.split(r"(do\(\)|don't\(\))", list_mul)
    add_next = False

    if "don't()" not in input_list[0]:
        to_multiply.append(input_list[0])

    for element in input_list[1:]:
        if "don't()" in element:
            add_next = False
        elif "do()" in element:
            add_next = True

        if add_next:
            to_multiply.append(element)

    pattern_mul = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    all_mul = re.findall(pattern_mul, "".join(to_multiply))
    for element in all_mul:
        a = int(element[0])
        b = int(element[1])
        result += a * b
    return result

print(repair_all_mul(string_lines)) # 75920122 too high

