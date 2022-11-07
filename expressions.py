def calc_math_expression(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    elif operator == ':':
        if num1 == 0 or num2 == 0:
            return None
        else:
            return num1 / num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return None


def calc_math_expression_from_str(str_input):
    data = str_input.split(" ")
    return calc_math_expression(num1=float(data[0]), num2=float(data[2]), operator=data[1])


def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    if (num1 >= num2) and (num1 >= num3):
        largest_number = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest_number = num2
    else:
        largest_number = num3

    if (num1 <= num2) and (num1 <= num3):
        smallest_number = num1
    elif (num2 <= num1) and (num2 <= num3):
        smallest_number = num2
    else:
        smallest_number = num3

    largest_and_smallest_number = (largest_number, smallest_number)
    return largest_and_smallest_number



#unable to complete 3. Quadratic equation Solver
#have removed code pertaining to this challenge as was not able to complete before 12am deadline




def temp_checker(min_temp, temp_1, temp_2, temp_3):
    days = [temp_1, temp_2, temp_3]
    if days[0] and days[1] > min_temp:
        return True
    elif days[0] and days[2] > min_temp:
        return True
    elif days[1] and days[2] > min_temp:
        return True
    else:
        return False

