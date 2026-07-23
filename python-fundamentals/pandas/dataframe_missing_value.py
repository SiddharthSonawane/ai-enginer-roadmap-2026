import pandas as pd

data = [
    {"product": "Laptop", "price": 75000, "category": "Electronics"},
    {"product": "Chair", "price": None, "category": "Furniture"},
    {"product": "Phone", "price": 45000, "category": None},
    {"product": "Desk", "price": None, "category": "Furniture"},
    {"product": "Tablet", "price": 32000, "category": "Electronics"}
]

df = pd.DataFrame(data)

# Task 1: Print count of missing values per column
# Task 2: Fill missing price with the mean price
# Task 3: Fill missing category with "Uncategorized"
# Task 4: Confirm no missing values remain using isnull().sum()


print(df.isnull().sum())
df_filled = df.fillna({
    "price": df["price"].mean(),
    "category": "Uncategorized",
})
print(df_filled)
print(df_filled.isnull().sum())