with open('./day2/input.txt', 'r') as file:
    lines = file.readlines()

# list_report = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"] # 2 qui devrait etre bien

def number_safe_report(list_report):
    result = 0
    for report in list_report:
        list_report = report.split()
        table_levels = [int(level) for level in list_report]
        if sorted(table_levels) == table_levels or sorted(table_levels)[::-1] == table_levels:
            if sorted(table_levels) == table_levels:
                initial_level = table_levels[0] - 1
                checklist = []
                for level in table_levels:
                    if 3 >= level - initial_level >= 1:
                        checklist.append(level)
                        initial_level = level
                if checklist == table_levels:
                    result += 1
            else:
                initial_level = table_levels[0] + 1
                checklist = []
                for level in table_levels:
                    if 3 >= initial_level - level >= 1:
                        checklist.append(level)
                        initial_level = level
                if checklist == table_levels:
                    result += 1
    return result

print(number_safe_report(lines))

