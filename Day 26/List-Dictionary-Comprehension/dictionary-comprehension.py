# Dictionary Comprehension - {new_key : new_value for item in list}
# Dictionary Comprehension - {new_key : new_value for (key, value) in dict.items()}
# Condition Dictionary Comprehension - {new_key : new_value for (key, value) in dict.items() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)
passed_students = {name: scores for (name, scores) in student_scores.items() if scores > 60}
print(passed_students)

