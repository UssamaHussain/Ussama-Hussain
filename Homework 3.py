# This is a sample Python script.
Task 1:
def longest_substring_without_duplicates(my_str):
    start = 0
    max_length = 0
    used_chars = {}

    for i, char in enumerate(my_str):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_chars[char] = i

    return max_length

# Example usage:
my_str = "hgfgklrmgfkg"
result = longest_substring_without_duplicates(my_str)
print(result)

Task2:
def reverse_integer(number):
    rev = 0
    while number > 0:
        rev = rev * 10 + number % 10
        number //= 10
    return rev

# Example usage:
number = 6842
result = reverse_integer(number)
print(result)

Task 3:
def smallest_missing_positive(numbers):
    nums = set(numbers)
    smallest = 1

    while smallest in nums:
        smallest += 1

    return smallest

# Example usage:
numbers1 = [1, 2, 4, 6, 5, 0]
result1 = smallest_missing_positive(numbers1)
print(result1)

numbers2 = [3, 4, -1, 1]
result2 = smallest_missing_positive(numbers2)
print(result2)

Task 4:
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:

            Task
            5:

            def calculate_grade(students):
                for reg_num, details in students.items():
                    homework = details['homework']
                    exam = details['exam']

                    total_grade = (homework + exam) / 10

                    if total_grade >= 8:
                        message = 'has passed, with final grade Excellent.'
                    elif 6 <= total_grade <= 7:
                        message = 'has passed, with final grade Good.'
                    elif 4 <= total_grade <= 5:
                        message = 'has passed, with final grade Acceptable.'
                    else:
                        message = 'has failed.'

                    print(f"The student with registration number {reg_num} {message}")

            # Input student details
            students = {
                'A1': {'homework': 15, 'exam': 68},
                'A2': {'homework': 7, 'exam': 18},
                'A3': {'homework': 14, 'exam': 48},
                'A4': {'homework': 20, 'exam': 40}
            }

            # Calculate grades and display results
            calculate_grade(students)
            merged.append(intervals[i])

    return merged

# Example usage:
intervals1 = [[1, 4], [3, 6], [9, 11], [14, 19]]
result1 = merge_intervals(intervals1)
print(result1)

intervals2 = [[1, 4], [3, 4], [4, 5]]
result2 = merge_intervals(intervals2)
print(result2)
