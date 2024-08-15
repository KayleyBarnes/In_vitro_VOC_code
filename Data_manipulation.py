import pandas as pd

file1 = pd.read_csv("pivoted_VOC_data.csv")

print(file1.head())

file2 = pd.read_csv("pivoted_VOC_data_Final_2.csv")

print(file1.head())

data = pd.merge(left=file1, right=file2, on=['Compound', 'ID'], how='inner')

print(data.head())

data.to_csv("Merged_data_file.csv", index=False)
