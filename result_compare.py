import pandas as pd

def calculate_mae(file1, file2):
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Ensure both DataFrames have the 'marker' column
    if 'marker' not in df1.columns or 'marker' not in df2.columns:
        print("Error: Both files must have a 'marker' column.")
        return

    # Ensure both DataFrames have the same number of rows
    if len(df1) != len(df2):
        print("Error: Both files must have the same number of rows.")
        return

    # Calculate Mean Absolute Error (MAE)
    total_difference = 0
    total_rows = len(df1)

    for index, row in df1.iterrows():
        marker1 = row['marker']
        marker2 = df2.iloc[index]['marker']
        if marker1 != marker2:
            total_difference += 1

    mae = total_difference / total_rows

    # Output results
    print("FOR BINARY")
    print("Total Difference:", total_difference)
    print("Total Rows:", total_rows)
    print("MAE (Mean Absolute Error):", mae)
    print("Percentage of Total Difference over Total Rows:", (total_difference / total_rows) * 100, "%")



def calculate_mae_multi(file1, file2):
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Ensure both DataFrames have the 'marker' column
    if 'marker' not in df1.columns or 'marker' not in df2.columns:
        print("Error: Both files must have a 'marker' column.")
        return

    # Ensure both DataFrames have the same number of rows
    if len(df1) != len(df2):
        print("Error: Both files must have the same number of rows.")
        return

    # Calculate Mean Absolute Error (MAE)
    total_difference = 0
    total_rows = len(df1)

    for index, row in df1.iterrows():
        marker1 = row['marker']
        marker2 = df2.iloc[index]['marker']
        if marker1 != marker2:
            total_difference += 1

    mae = total_difference / total_rows

    # Output results
    print("FOR MULTI")
    print("Total Difference:", total_difference)
    print("Total Rows:", total_rows)
    print("MAE (Mean Absolute Error):", mae)
    print("Percentage of Total Difference over Total Rows:", (total_difference / total_rows) * 100, "%")


# Replace file paths with your file names
file1 = "TestingResultsBinary.csv"
file2 = "binary_groundtruth.csv"

calculate_mae(file1, file2)

# # Replace file paths with your file names
file1_multi = "TestingResultsMulti.csv"
file2_multi = "multi_groundtruth.csv"

calculate_mae_multi(file1_multi, file2_multi)