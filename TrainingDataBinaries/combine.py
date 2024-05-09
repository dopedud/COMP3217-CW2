import pandas as pd
from pathlib import Path

# Get the current working directory
current_dir = Path.cwd() / 'TrainingDataBinaries'

# Initialize an empty list to store the data frames
dfs = []

# Loop through the CSV files
for i in range(1, 16):
    file_name = f'data{i}.csv'
    file_path = current_dir / file_name

    # Check if the file exists
    if file_path.is_file():
        # Read the CSV file into a data frame
        df = pd.read_csv(file_path)

        # Remove the first row (column headings) if it's not data1.csv
        if i > 1:
            df = df.iloc[1:].reset_index(drop=True)

        # Append the data frame to the list
        dfs.append(df)
    else:
        print(f"File '{file_name}' not found in the current directory.")

# Concatenate all data frames in the list
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined data frame to a new CSV file
combined_df.to_csv('TrainingDataBinaries/combined_data.csv', index=False)