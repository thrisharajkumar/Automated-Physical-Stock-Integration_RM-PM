%pip install openpyxl
import pandas as pd

# Read the first Excel file
df1 = pd.read_excel("file1.xlsx")

# Read the second Excel file
df2 = pd.read_excel("file2.xlsx")

# Find the maximum batch number for each material code in the first Excel file
max_batch_df = df1.groupby('Material')['Batch'].max().reset_index()

# Merge with the first Excel file to get the corresponding rows
result_df = pd.merge(df1, max_batch_df, on='Material', how='left')

# Merge the result with the second Excel file to get the physical stock value
result_df = pd.merge(result_df, df2[['Material', 'Physical Stock']], on='Material', how='left')

# Fill NaN values in the "Physical Stock" column with 0
result_df['Physical Stock'] = result_df.apply(lambda row: row['Physical Stock'] if row['Batch_x'] == row['Batch_y'] else 0, axis=1)

# Drop the Batch_y column as it's no longer needed
result_df.drop(columns=['Batch_y'], inplace=True)

# Rename Batch_x to Batch
result_df.rename(columns={'Batch_x': 'Batch'}, inplace=True)

# Save the result to a new Excel file
result_df.to_excel("result.xlsx", index=False)
