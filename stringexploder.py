import sys
import math

__author__ = 'shaibo'

# Populates the numeric counter used to generate all binary values
def getNumericCounter(input):
    numeric_counter = []
    for c in input:
        if c!= '1' and c != '0' and c !='X':
            sys.stdout.write(c + ' is illegal\n')
            sys.exit(1)

        if c == 'X':
            numeric_counter.append(0)

    return numeric_counter

# Increments a counter which is used to populate the characters instead of X
def incrementCount(input_numeric_counter, counter_size):
    carry = False
    for i in reversed(range(counter_size)):
        if input_numeric_counter[i] == 0:
            input_numeric_counter[i] = 1
            carry = False
        elif input_numeric_counter[i] == 1:
            input_numeric_counter[i] = 0
            carry = True
        if carry == False:
            break

# Fills in the X characters with the relevant digit of the counter
def mergeAndPrint(input_str, input_numeric_counter):
    counter_index = 0
    for c in input_str:
        if c == 'X':
            sys.stdout.write(str(input_numeric_counter[counter_index]))
            counter_index += 1
        else:
            sys.stdout.write(c)
    sys.stdout.write('\n')

# Counts and prints all permutations
def incrementAndPrint(input_str, input_numeric_counter, counter_size, count):
    index = 0
    #starting with all 0's
    if counter_size > 0:
        mergeAndPrint(input_str, input_numeric_counter)

    while index < count - 1:
        incrementCount(input_numeric_counter, counter_size)
        #print next combination
        mergeAndPrint(input_str, input_numeric_counter)
        index += 1


# Execution:
if len(sys.argv) < 2:
    sys.stderr.write('No parameters were provided\n')
    sys.exit(1)

user_input = sys.argv[1]

input_numeric_counter = getNumericCounter(user_input)

counter_size = len(input_numeric_counter)
iteration_count = math.pow(2, counter_size)

incrementAndPrint(user_input, input_numeric_counter, counter_size, iteration_count)

sys.stdout.write('done\n')
