from io import StringIO
import pandas as pd

# Create CSV data in memory
csv_data = """Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago"""

# Convert string into a file-like object
data = StringIO(csv_data)

# Check type
print("Type of data:", type(data))

# Read CSV into DataFrame
df = pd.read_csv(data)

print("\nDataFrame:")
print(df)

# Check DataFrame type
print("\nType of df:", type(df))

# Convert DataFrame back to CSV and read again
csv_string = df.to_csv(index=False)

print("\nDataFrame converted back to CSV and read again:")
print(pd.read_csv(StringIO(csv_string)))

# Reset StringIO pointer to beginning before reading again
data.seek(0)

# Read only selected columns
print("\nSelected Columns:")
print(pd.read_csv(data, usecols=['Name', 'City']))

# df.to_csv('example.csv')
print(data)


print(df['Name'][2]) #print the value in the 'Name' column of the third row (index 2) of the dataframe

