import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("house_price.csv")

# Split dataset
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

# Create train.db
train_conn = sqlite3.connect("databases/train.db")
train_df.to_sql(
    "houses",
    train_conn,
    if_exists="replace",
    index=False
)
train_conn.close()

# Create test.db
test_conn = sqlite3.connect("databases/test.db")
test_df.to_sql(
    "houses",
    test_conn,
    if_exists="replace",
    index=False
)
test_conn.close()

print("train.db and test.db created successfully")