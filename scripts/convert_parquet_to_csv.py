import pandas as pd

# 🔁 Replace the file name below with the actual name if it's different
input_file = 'run-1750454037807-part-block-0-r-00000-snappy.parquet'
output_file = 'converted_output.csv'

# Load the Parquet file using pandas
df = pd.read_parquet(input_file)

# Save it as CSV (without index column)
df.to_csv(output_file, index=False)

print(f"✅ CSV file has been saved as: {output_file}")
