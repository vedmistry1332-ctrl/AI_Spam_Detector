import pandas as pd

# Read the original dataset
df = pd.read_csv(
    "dataset/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Save it as CSV
df.to_csv("dataset/spam.csv", index=False)

print("Dataset converted successfully!")
print(df.head())