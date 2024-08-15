###Open “Merged_data_file.csv” in excel and add presence x and presence y in a new column called “Final_presence” then reopen file in python (below)

presence2 = pd.read_csv("Merged_data_file.csv ")

presence2_pivot = pd.pivot_table(presence2, values="Final_presence", index="ID", columns="Compound")

print(presence2_pivot.head())

presence2_pivot.to_csv("presence2_pivot.csv", index=True)
  
