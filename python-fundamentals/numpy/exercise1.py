import numpy as np

temps = np.array([30, 45, 60, 75, 90, 15])

# Task: Using boolean masking, get all temps that are between 40 and 80 (inclusive)
# Hint: you can combine two conditions using & like this:
# arr[(condition1) & (condition2)]

controlled_temps = temps[(temps >= 40) & (temps <= 80)]
print(f"Temperatures between 40 and 80: {controlled_temps}")