valid_inputs = [0, 20, 40, 60, 80, 100, 120]
pass_credits = 0
defer_credits = 0
fail_credits = 0
progress_count = 0
module_trailer_count = 0
exclude_count = 0
do_not_progress_count = 0
loop_count = 0
progess_list = []
module_trailer_list = []
exclude_list = []
do_not_progress_list = []
student_results = {}
total = 0


# Validating functions -------------------------------------------
def validate_range():
    if not (any(i in inputs for i in valid_inputs)):
        print("Out of range.")
        exit()


def validate_total():
    if total != 120:
        print("Total incorrect.")
        exit()


# Status functions -----------------------------------------------

def progress():
    if pass_credits == 120:
        global progress_count
        print("Progress")
        print('')
        progess_list.append(inputs)
        progress_count += 1
        list_to_str = ', '.join([str(elements) for elements in inputs])
        student_results[id_number] = "Progress - ", list_to_str


def module_trailer():
    if pass_credits == 100:
        global module_trailer_count
        print("Progress (module trailer)")
        print('')
        module_trailer_list.append(inputs)
        module_trailer_count += 1
        list_to_str = ', '.join([str(elements) for elements in inputs])
        student_results[id_number] = "Progress (module trailer) - ", list_to_str


def exclude():
    if 80 <= fail_credits <= 120:
        global exclude_count
        print("Exclude")
        print('')
        exclude_list.append(inputs)
        exclude_count += 1
        list_to_str = ', '.join([str(elements) for elements in inputs])
        student_results[id_number] = "Exclude - ", list_to_str


def do_not_progress():
    if 0 <= pass_credits <= 80 and fail_credits < 80:
        global do_not_progress_count
        print("Module retriever")
        print('')
        do_not_progress_list.append(inputs)
        do_not_progress_count += 1
        list_to_str = ', '.join([str(elements) for elements in inputs])
        student_results[id_number] = 'Module retriever - ', list_to_str


def get_input_and_validate_type(section, credit):
    try:

        credit = int(input("Please enter your credits at " + section + " : "))

    except:
        print("Integer required")
        exit()

    inputs.append(credit)
    validate_range()
    return credit


def check_id():  # check the id number is already used.
    global id_number
    while id_number in student_results:
        print("Id number already exists")
        id_number = input("Enter your ID number : ")


loop = 'y'

while loop == 'y' and loop != 'q':
    loop_count += 1
    inputs = []
    id_number = input("Enter your ID number : ")
    check_id()

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

    while loop != 'q':
        print("Would you like to enter another set of data?")
        loop = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
        if loop == 'y':
            break

if loop == 'q':
    print("Part 4 : ")
    for key, value in student_results.items():
        print(key, ': ',*value,sep='')

    exit()
