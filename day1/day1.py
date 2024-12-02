with open('/Users/borislebon/Documents/13. PROGRAMMATION/programmation/Python/test_technique/advent_of_code_2024/day1/input.txt', 'r') as file:
    lines = file.readlines()
    left_list = []
    right_list = []
    for element in lines:
        left_list.append(int(element.split()[0]))
        right_list.append(int(element.split()[1]))



def find_list_gap(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    all_distance = []
    for number1, number2 in zip(sorted_list1, sorted_list2):
        if number1 >= number2:
            distance = number1 - number2
        else:
            distance = number2 - number1
        all_distance.append(distance)
    result = 0
    for distance in all_distance:
        result += distance
    return result

print(find_list_gap(left_list, right_list))