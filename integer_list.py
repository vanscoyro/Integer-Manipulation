def read_integer_list():
    # Read a list of integers from the user as a string
    input_str = input("Enter a list of integers, seperated by spaces: ")

    # Split the string into a list of integers
    integer_list = [int(x) for x in input_str.split()]

    # Return the list of integers
    return integer_list

def calculate_mean(integer_list):
    # Initialize a sum variable
    sum = 0

    # Iterate over the list and add up all the elements
    for x in integer_list:
        sum += x

    # Calculate the mean by dividing the sum by the length of the list
    return sum / len(integer_list)

def calculate_median(integer_list):

    # If the length of the list is odd, the median is the middle element
    if len(integer_list) % 2 == 1:
        # Calculate the index of the middle element
        median_index = len(integer_list) // 2
        # Return the middle element
        return integer_list[median_index]

    else:
        # Calculate the indexes of the two middle elements
        median_index1 = len(integer_list) // 2 - 1
        median_index2 = len(integer_list) // 2
        # Return the average of the two middle elements
        return (integer_list[median_index1] + integer_list[median_index2]) / 2


def calculate_mode(integer_list):
    # Create a dictionary to count the frequency of each element
    frequency_count = {}
    for x in integer_list:
        if x in frequency_count:
            frequency_count[x] += 1
        else:
            frequency_count[x] = 1

    # Find the element with the highest frequency
    mode = None
    highest_frequency = 0
    for x, frequency in frequency_count.items():
        if frequency > highest_frequency:
            mode = x
            highest_frequency = frequency

    # Return the mode
    return mode


# Read a list of integers from the user
integer_list = read_integer_list()

# Calculate the mean of the list of integers
mean = calculate_mean(integer_list)

# Calculate the median of the list of integers
median = calculate_median(integer_list)

# Calculate the mode of the list of integers
mode = calculate_mode(integer_list)

# Print the mean median and mode
print(f"The mean is {mean}")
print(f"The median is {median}")
print(f"The mode is {mode}")
