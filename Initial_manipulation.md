Prior to data manipulation the individual .csv files obtained for each individual seaweed from the SPME analysis were compiled into one .csv file per replicate. 
With the seaweed ID in column 1 and compound ID in column 2. 
Using the following 


```
## Using bash 
## Extract column B from all files - this is the compound name
for i in *.csv; do cut -f2 -d ',' $i  >  $i.csv; done

# puts seaweed name in column 1 of files
for file in *.csv.csv; do
    awk -v filename="$file" 'BEGIN{FS=OFS=","} {print filename, $0}' "$file" > "modified_$file"
done

# now combine files together into a single file
cat modified*.csv > replicate1.csv
```
The same was done for replicate 2 data 

Then python merge of the two replicate files 
```
import pandas as pd

file1 = pd.read_csv("pivoted_VOC_data.csv")

print(file1.head())

file2 = pd.read_csv("pivoted_VOC_data_Final_2.csv")

print(file1.head())

data = pd.merge(left=file1, right=file2, on=['Compound', 'ID'], how='inner')

print(data.head())

data.to_csv("Merged_data_file.csv", index=False)

```

Open 'Merged_data_file.csv' in excel and add Replicate1 presence column and Replicate2 presence column, additional column named 'Final_presence'

