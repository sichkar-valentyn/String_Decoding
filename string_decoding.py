# Implementing the task
# Decoding input string
# Example
# Input string: 3a5Ba4CcF3f
# Decoded string: aaaBBBBBaCCCCcFfff
# Also, program will check if the number has more then one digit
# This task is so called basic compressing task


# Creating a function for dividing input string by groups
def string_grouping(input_string):
    # Checking if input string is just a one letter
    if len(input_string) == 1:
        return input_string
    else:
        # Creating a list to add grouped elements
        lst = []
        # Variable for iteration
        i = 0
        # Going through elements of the string
        while True:
            # Checking if the element is a digit and the next element is not a digit
            if input_string[i].isdigit() and not input_string[i + 1].isdigit():
                lst += [int(input_string[i]) * input_string[i + 1]]
                i += 2
            # Checking if number has more then one digit
            elif input_string[i].isdigit() and input_string[i + 1].isdigit():
                # Collecting all digits together
                # Variable for number
                number = ''
                # Variable for iteration
                j = i
                while True:
                    if input_string[j].isdigit():
                        number += input_string[j]
                        j += 1
                    else:
                        lst += [int(number) * input_string[j]]
                        break
                i = j + 1
            else:
                lst += [input_string[i]]
                i += 1
            if i >= len(input_string):
                break
    return lst


# Input string and returning decoded result
print(''.join(string_grouping(input())))

