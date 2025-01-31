#Converts a decimal number to binary
import math
def decimal_to_binary(number):
    binary_num = []
    num = number
    while num > 0:
        #Extract the remainder first and add it to the list
        if num % 2 == 0:
            binary_num.append(0)
        elif num % 2 == 1:
            binary_num.append(1)
        #Divide the number and then round down until it reaches zero
        rounded_number = math.floor(num / 2)
        num = rounded_number
    return convert_list(binary_num) #Calls the convert_list function to flip the list

def convert_list(binary_list):

    # Flips the list since binary numbers are read from right to left
    flip_binary_number = binary_list[::-1 ]
    # The list of integers are then converted to strings
    convert_to_string = [str(bit) for bit in flip_binary_number]
    
    output_binary = ''
    for str_bit in convert_to_string:
        output_binary += str_bit
    # Returns a cleaner output
    return output_binary

number_to_binary = int(input('Enter a number to convert to binary: '))
conversion = decimal_to_binary(number_to_binary)
print(f'\n{number_to_binary} in binary is: 0b{conversion}')
