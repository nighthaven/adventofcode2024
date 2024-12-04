with open('./day2/input.txt', 'r') as file:
    lines = file.readlines()

list_report = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"] # 4 qui devrait etre bien


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


def is_sorted_with_intruder(liste):
    intrus = 0
    for i in range(1, len(liste)):
        if liste[i] < liste[i - 1]:
            intrus += 1
            if intrus > 1:
                return False
    return True

def is_reversed_with_intruder(liste):
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
        report_list = report.split()
        table_levels = [int(level) for level in report_list]


        if security_level_limit(table_levels):
            if is_increasing(table_levels):
                if is_sorted_with_intruder(table_levels):
                    result += 1
            else:
                if is_reversed_with_intruder(table_levels):
                    result += 1

    return result

print(number_safe_report(lines)) # 605 too high 305 wrong

