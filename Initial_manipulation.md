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

See Pivot_data.py for next step


