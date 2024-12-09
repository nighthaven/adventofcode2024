# NOT FINISHED

with open('./day2/input.txt', 'r') as file:
    lines = file.readlines()

list_report = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"] # 4 qui devrait etre bien
list_report_2 = ["48 46 47 49 51 54 56", "1 1 2 3 4 5", "1 2 3 4 5 5", "5 1 2 3 4 5", "1 4 3 2 1", "1 6 7 8 9", "1 2 3 4 3", "9 8 7 6 7", "7 10 8 10 11", "29 28 27 25 26 25 22 20"]
# 1 : oui,  2 : oui, 3 : oui, 4 : non, 5: oui, 6: non, 7 : oui , 8 : oui, 9: AIE non 10: oui total 7

def security_level_limit(liste):
    for i in range(1, len(liste)):
        if abs(liste[i] - liste[i - 1]) > 3:
            return False
    return True

def is_increasing(liste):
    increase = 0
    for i in range(1, len(liste)):
        increase += 1
        if liste[i] < liste[i - 1]:
            increase -= 1
    if increase <= 1:
        return False
    return True

def is_decreasing(liste):
    decrease = 0
    for i in range(1, len(liste)):
        decrease += 1
        if liste[i] > liste[i - 1]:
            decrease -= 1
    if decrease <= 1:
        return False
    return True

def is_sorted_with_one_intruder(liste):
    intrus = 0
    for i in range(len(liste)):
        check_list = liste[:]
        del check_list[i]
        if check_list == sorted(check_list):
            continue
        intrus += 1
    if intrus > 1:
        return False
    return True

def is_reversed_with_one_intruder(liste):
    intrus = 0
    for i in range(len(liste)):
        check_list = liste[:]
        del check_list[i]
        if check_list == sorted(check_list)[::-1]:
            continue
        intrus += 1
    if intrus > 1:
        return False
    return True



def is_sorted_with_intruder(liste):
    check_list = liste[:]
    del check_list[0]
    if check_list == sorted(liste):
        return True

    intrus = 0
    for i in range(1, len(liste)):
        if liste[i] < liste[i - 1]:
            intrus += 1
            if intrus > 1:
                return False
    return True

def is_reversed_with_intruder(liste):
    check_list = liste[:]
    del check_list[0]
    if check_list == reversed(liste):
        return True
    intrus = 0
    for i in range(1, len(liste)):
        if liste[i] > liste[i - 1]:
            intrus += 1
            if intrus > 1:
                return False
    return True


def number_safe_report(list_report):
    result = 0
    for report in list_report:
        table_levels = [int(level) for level in report.split()]
        if security_level_limit(table_levels):
            if is_increasing(table_levels):
                if is_sorted_with_one_intruder(table_levels):
                    result += 1
            elif is_decreasing(table_levels):
                if is_reversed_with_one_intruder(table_levels):
                    result += 1

    return result

print(number_safe_report(list_report)) # 605 too high 305 wrong

# NOT FINISHED