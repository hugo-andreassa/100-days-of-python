import random


numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
# print(new_list)

range_list = [num * 2 for num in range(1, 101)]
# print(range_list)

# Conditionals ----------------------------------------------------------------
range_list_with_condition = [num for num in range(1, 51) if num % 2 == 0]
# print(range_list_with_condition)

# List Comprehension 1 Challenge ----------------------------------------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

# List Comprehension 2 Challenge ----------------------------------------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# List Comprehension 3 Challenge ----------------------------------------------
with open("file1.txt") as file1:
    file1_numbers = [num for num in file1.readlines()]

with open("file2.txt") as file2:
    file2_numbers = [num for num in file2.readlines()]
result = [int(num) for num in file1_numbers if num in file2_numbers]
# print(result)

# Dictionary Comprehension ----------------------------------------------------
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor']
students_score = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(students_score)
# print(passed_students)

# Dictionary Comprehension 1 Challenge ----------------------------------------
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result_challenge_1 = {letter: len(letter) for letter in sentence.split(" ")}
# print(result_challenge_1)

# Dictionary Comprehension 2 Challenge ----------------------------------------
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: ((temp * 9/5) + 32) for (day, temp) in weather_c.items()}

print(weather_f)
























