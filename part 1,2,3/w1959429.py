valid_inputs = [0, 20, 40, 60, 80, 100, 120]
pass_credits = 0
defer_credits = 0
fail_credits = 0
progress_count = 0
module_trailer_count = 0
exclude_count = 0
do_not_progress_count = 0
loop_count = 0
progress_list = []
module_trailer_list = []
exclude_list = []
do_not_progress_list = []
total = 0


# Validating functions(validate range and the total)

def validate_range():
    if not (any(i in inputs for i in valid_inputs)):
        print("Out of range.")
        exit()


def validate_total():
    if total != 120:
        print("Total incorrect.")
        exit()


# Status functions (These functions predicts the module type and appending data into related lists)

def progress():
    if pass_credits == 120:
        global progress_count
        print("Progress")
        print('')
        progress_list.append(inputs)
        progress_count += 1


def module_trailer():
    if pass_credits == 100:
        global module_trailer_count
        print("Progress (module trailer)")
        print('')
        module_trailer_list.append(inputs)
        module_trailer_count += 1


def exclude():
    if 80 <= fail_credits <= 120:
        global exclude_count
        print("Exclude")
        print('')
        exclude_list.append(inputs)
        exclude_count += 1


def do_not_progress():
    if 0 <= pass_credits <= 80 and fail_credits < 80:
        global do_not_progress_count
        print("Do not Progress-module retriever")
        print('')
        do_not_progress_list.append(inputs)
        do_not_progress_count += 1


def part2_output(list, str_type):  # printing process in part 2
    for elements in list:
        i = 0
        list_to_str = ', '.join([str(elements) for elements in elements])  # get rid of brackets
        print(str_type, list_to_str)
        i += 1


def part3_output(list, type):  # This function append data to the file.

    for elements in list:
        i = 0
        with open('output.txt', 'a') as file:
            list_to_str = ', '.join([str(elements) for elements in elements])
            file.write(type)
            file.write(list_to_str)
            file.write('\n')
        i += 1


# In below function, It Gets the user inputs and do the range validation part.

def get_input_and_validate_type(section, credit):
    try:
        credit = int(input("Please enter your credits at " + section + " : "))

    except:
        print("Integer required")
        exit()
    inputs.append(credit)
    validate_range()
    return credit


loop = 'y'

while loop == 'y' and loop != 'q':  # This loop is to continue the process until user enters 'q'
    loop_count += 1
    inputs = []

    pass_credits = get_input_and_validate_type("pass", pass_credits)
    total += pass_credits
    defer_credits = get_input_and_validate_type("defer", defer_credits)
    total += defer_credits
    fail_credits = get_input_and_validate_type("fail", fail_credits)
    total += fail_credits

    validate_total()
    total = 0
    progress()
    do_not_progress()
    module_trailer()
    exclude()

    while loop != 'q':  # loops until the user input a valid option
        print("Would you like to enter another set of data?")
        loop = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
        if loop == 'y':
            break

# Histogram

if loop == 'q':
    print("")
    print("Histogram")
    print("Progress ", progress_count, ' :', "*" * progress_count)
    print("Trailer ", module_trailer_count, '  :', "*" * module_trailer_count)
    print("Retriever ", do_not_progress_count, ':', "*" * do_not_progress_count)
    print("Excluded ", exclude_count, ' :', "*" * exclude_count)
    print('')
    print(loop_count, "outcomes in total.")
    print("")

# part 2 - getting output from lists.

print("part 2: \n")
part2_output(progress_list, 'Progress - ')
part2_output(module_trailer_list, 'Progress (module trailer) - ')
part2_output(do_not_progress_list, 'Module retriever - ')
part2_output(exclude_list, 'Exclude - ')

# part 3 - getting output from file

with open('output.txt', 'w') as file:
    file.write('part 3 : \n')

part3_output(progress_list, 'Progress - ')
part3_output(module_trailer_list, 'Progress (module trailer) - ')
part3_output(do_not_progress_list, 'Module retriever - ')
part3_output(exclude_list, 'Exclude - ')

with open('output.txt', 'r') as file:
    lines = file.read()
    print("")
    print(lines)
