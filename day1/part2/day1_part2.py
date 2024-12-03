with open('./day1/input.txt', 'r') as file:
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
        count_number = sorted_list2.count(number1)
        all_distance.append(number1*count_number)
    result = 0
    for distance in all_distance:
        result += distance
    return result

print(find_list_gap(left_list, right_list)) # 19457120