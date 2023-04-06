import os
import pandas as pd

# Set the path to the folder containing the CSV files
folder_path = "path-to-folder-containing-all-csv-files"

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Create an empty list to store the dataframes
list_of_dfs = []

# Loop through each CSV file and read it into a dataframe
for csv_file in csv_files:
    csv_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(csv_path)
    list_of_dfs.append(df)

# Concatenate all dataframes into a single dataframe
result = pd.concat(list_of_dfs, axis=1, ignore_index=True)

# Write the concatenated dataframe to a new CSV file
result.to_csv("path-to-output-folder-for-csv/output.csv", index=False)