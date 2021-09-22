# read corpus.txt

corpus = open("corpus.txt", "r")

possible_variable_candiates = []

# read every line in corpus.txt and sanitize it to possible_variable_candiates
for line in corpus:
    line = line.strip()
    line = line.split()
    for word in line:
        if word.isalpha() and len(word) > 1:
            possible_variable_candiates.append(word)

possible_statements = [
    "LET",
    "PRINT",
    "PRINTALL",
    "ADD",
    "SUB",
    "MULT",
    "DIV",
    "GOTO",
    "IF",
    "GOSUB",
    "RETURN",
]

import os
from monkeyspanner import synthesize_statement, get_random_int_within

TEST_CASE_NUM = 100

for x in range(TEST_CASE_NUM):
    # Get Random Number from 0 to 999
    program_length = get_random_int_within(0, 999)
    program_lines = []
    # Get Random Number from 0 to len(possible_statements)
    for y in range(program_length):
        statement = possible_statements[
            get_random_int_within(0, len(possible_statements) - 1)
        ]
        program_lines.append(
            f"{y+1} {synthesize_statement(statement, possible_variable_candiates)}"
        )

    # Create input folder if it doesn't exist
    if not os.path.exists("input"):
        os.makedirs("input")

    # Write program_lines to a file
    program_file = open(f"input/input{x + 1}.txt", "w")
    for line in program_lines:
        program_file.write(line + "\n")
    program_file.close()
