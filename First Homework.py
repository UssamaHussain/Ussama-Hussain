Task 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def calculate_average(prime_list):
    if not prime_list:
        return 0
    return sum(prime_list) / len(prime_list)

start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

prime_numbers = find_primes(start_num, end_num)
average = calculate_average(prime_numbers)

print("Prime numbers between", start_num, "and", end_num, "are:", prime_numbers)
print("The average of these prime numbers is:", average)

Task 2
def calculate_formula(N):
    result = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            result += i ** 3
        else:
            result += i ** 2
    return result

N = int(input("Enter a positive integer N: "))
formula_result = calculate_formula(N)
print("The result of the formula is:", formula_result)

Task 3
def rotate_array(arr, direction, d):
    length = len(arr)
    if direction == 'left':
        d = d % length
        arr = arr[d:] + arr[:d]
    elif direction == 'right':
        d = d % length
        arr = arr[-d:] + arr[:-d]
    return arr

# Input array
arr = [1, 2, 3, 4, 5, 6, 7]

# User inputs
direction = input("Enter the direction ('left' or 'right'): ")
d = int(input("Enter the number of elements to rotate: "))

rotated_array = rotate_array(arr, direction, d)
print("Output after rotation:", rotated_array)

Task 4
def rotate_2d_array(arr, shift_type, direction, index, d):
    rows = len(arr)
    cols = len(arr[0])

    if shift_type == 'row':
        index %= rows
        if direction == 'left':
            arr[index] = arr[index][d % cols:] + arr[index][:d % cols]
        elif direction == 'right':
            arr[index] = arr[index][-d % cols:] + arr[index][:-d % cols]
    elif shift_type == 'column':
        index %= cols
        column = [arr[i][index] for i in range(rows)]
        if direction == 'top':
            column = column[d % rows:] + column[:d % rows]
        elif direction == 'down':
            column = column[-d % rows:] + column[:-d % rows]
        for i in range(rows):
            arr[i][index] = column[i]

    return arr

# Input 2D array
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# User inputs
shift_type = input("Row or column shift? ('row' or 'column'): ")
direction = input("Direction ('left', 'right', 'top', 'down'): ")
index = int(input("Index of row or column: "))
num_elements = int(input("Number of elements to shift: "))

shifted_array = rotate_2d_array(array_2d, shift_type, direction, index, num_elements)
print("Output after shift:")
for row in shifted_array:
    print(row)

Task 5
def split_and_rotate(arr, index):
    if index >= len(arr):
        return arr
    return arr[index:] + arr[:index]

# Input list
original_list = [1, 2, 3, 4, 5, 6, 7]

# User input
split_index = int(input("Enter the index to split the list: "))

new_list = split_and_rotate(original_list, split_index)
print("New list after splitting and rotating:", new_list)
