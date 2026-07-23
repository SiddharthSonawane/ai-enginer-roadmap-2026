import pandas as pd

employees = [
    {"name": "Amit", "department": "Engineering", "salary": 85000},
    {"name": "Sara", "department": "Marketing", "salary": 72000},
    {"name": "Ravi", "department": "Engineering", "salary": 91000},
    {"name": "Priya", "department": "HR", "salary": 65000},
    {"name": "John", "department": "Marketing", "salary": 78000}
]

df = pd.DataFrame(employees)

# Task 1: Print the shape of the DataFrame
# Task 2: Print only the "name" column
# Task 3: Filter and print only Engineering department employees
# Task 4: Add a new column "salary_in_lakh" converting salary (divide by 83, approx USD to INR/lakh conversion)
# Task 5: Print df.info() and observe what it tells you

print(f"Shape of the DataFrame: {df.shape}")
print(f"Names of employees:\n{df['name']}")
engineering_employees = df[df['department'] == 'Engineering']
print(f"Engineering employees:\n{engineering_employees}")
df['salary_in_lakh'] = df['salary'] / 83
print(f"Salaries in lakh column added:\n{df}")
print(df.info())