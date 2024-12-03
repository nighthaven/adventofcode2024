with open('./day3/input.txt', 'r') as file:
    lines = file.readlines()

list_input = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]

import re

def repair_all_mul(list_mul):
    result = 0
    for input in list_mul:
        pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
        all_mul = re.findall(pattern, input)
        for element in all_mul:
            a = int(element[0])
            b = int(element[1])
            result += a * b
    return result


print(repair_all_mul(lines)) # 156388521