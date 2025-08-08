import pandas as pd

df = pd.read_csv("data/raw_data.csv")
df["budget_per_student"] = df["budget"] / df["student_count"]
df.to_csv("data/cleaned_data.csv", index=False)
