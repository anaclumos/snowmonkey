from random import randint, sample


def synthesize_statement(statement, varlist):
    if statement == "LET":
        return synthesize_let_statement(get_random_vars(varlist, num=1))
    elif statement == "PRINT":
        return synthesize_print_statement(get_random_vars(varlist, num=1))
    elif statement == "PRINTALL":
        return synthesize_printall_statement()
    elif statement == "ADD":
        return synthesize_add_statement(get_random_vars(varlist, num=2))
    elif statement == "SUB":
        return synthesize_sub_statement(get_random_vars(varlist, num=2))
    elif statement == "MULT":
        return synthesize_mult_statement(get_random_vars(varlist, num=2))
    elif statement == "DIV":
        return synthesize_div_statement(get_random_vars(varlist, num=2))
    elif statement == "GOTO":
        return synthesize_goto_statement()
    elif statement == "IF":
        return synthesize_if_statement(get_random_vars(varlist, num=2))
    elif statement == "GOSUB":
        return synthesize_gosub_statement()
    elif statement == "RETURN":
        return synthesize_return_statement()
    else:
        return "ERROR"


def get_random_vars(varlist, num):
    return sample(varlist, num)


def get_random_int():
    # With a 60% chance, returns 0-1000
    # With a 40% chance, returns INT.Min - INT.Max
    if randint(0, 100) < 60:
        return randint(0, 1000)
    else:
        return randint(-2147483648, 2147483647)


def get_random_int_within(min, max):
    return randint(min, max)


def synthesize_let_statement(var):
    if len(var) == 1:
        return "LET " + str(var[0]) + " " + str(get_random_int())
    else:
        return "ERROR"


def synthesize_print_statement(var):
    if len(var) == 1:
        return "PRINT " + str(var[0])
    else:
        return "ERROR"


def synthesize_printall_statement():
    return "PRINTALL"


def synthesize_add_statement(var):
    if get_random_int_within(0, 2) == 0:
        return "ADD " + str(var[0]) + " " + str(get_random_int())
    else:
        return "ADD " + str(var[0]) + " " + str(var[1])


def synthesize_sub_statement(var):
    if get_random_int_within(0, 2) == 0:
        return "SUB " + str(var[0]) + " " + str(get_random_int())
    else:
        return "SUB " + str(var[0]) + " " + str(var[1])


def synthesize_mult_statement(var):
    if get_random_int_within(0, 2) == 0:
        return "MULT " + str(var[0]) + " " + str(get_random_int())
    else:
        return "MULT " + str(var[0]) + " " + str(var[1])


def synthesize_div_statement(var):
    case = get_random_int_within(0, 3)
    if case == 0:
        return "DIV " + str(var[0]) + " " + str(get_random_int())
    elif case == 1:
        return "DIV " + str(var[0]) + " 0"
    else:
        return "DIV " + str(var[0]) + " " + str(var[1])


def synthesize_goto_statement():
    return "GOTO " + str(get_random_int())


def synthesize_if_statement(var):
    possible_operators = ["<", "<=", ">", ">=", "=", "<>"]
    operator = str(sample(possible_operators, 1)[0])
    case = get_random_int_within(0, 4)

    # check if var[0] and var[1] are string
    if type(var[0]) == str or type(var[1]) == str:
        if case == 0:
            statement = f"IF {get_random_int()} {operator} {get_random_int()} THEN {get_random_int()}"
            return statement
        elif case == 1:
            statement = (
                f"IF {var[0]} {operator} {get_random_int()} THEN {get_random_int()}"
            )
            return statement
        elif case == 2:
            statement = (
                f"IF {get_random_int()} {operator} {var[1]} THEN {get_random_int()}"
            )
            return statement
        else:
            statement = f"IF {var[0]} {operator} {var[1]} THEN {get_random_int()}"
            return statement


def synthesize_gosub_statement():
    return "GOSUB " + str(get_random_int())


def synthesize_return_statement():
    return "RETURN"
