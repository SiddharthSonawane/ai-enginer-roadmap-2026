import numpy as np

scores = np.array([85, 92, 78, 95, 88])

# Task 1: Print the average score
# Task 2: Print only scores above 90
# Task 3: Multiply every score by 1.1 (a 10% boost) and print the result

avg_score = scores.mean()
print(f"Average score: {avg_score}")

high_scores = scores[scores > 90]
print(f"Scores above 90: {high_scores}")

boosted_scores = scores * 1.1
print(f"Boosted scores: {boosted_scores}")