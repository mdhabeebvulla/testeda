import pandas as pd
import sys

# Load CSV
df = pd.read_csv("iris.csv")

# Define expected types
expected_types = {
    "sl": float,
    "sw": float,
    "pl": float,
    "pw": float,
    "species": str
}

# Check last row only (newly added)
new_sample = df.tail(1)

# 1. Null check
if new_sample.isnull().values.any():
    print("❌ Error: Null values found in the new sample.")
    sys.exit(1)

# 2. Data type check
for col, dtype in expected_types.items():
    if not isinstance(new_sample.iloc[0][col], dtype):
        print(f"❌ Error: Column '{col}' should be of type {dtype}. Got {type(new_sample.iloc[0][col])}.")
        sys.exit(1)

print("✅ New sample is valid.")
