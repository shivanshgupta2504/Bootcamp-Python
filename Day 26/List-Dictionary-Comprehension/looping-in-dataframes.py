import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

# Loop through DataFrames
for (key, val) in student_df.items():
    print(key)
    print(val)

# looping through rows of DataFrames
for (index, row) in student_df.iterrows():
    print(row.score)
