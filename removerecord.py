# this tool removes duplicate records listed in one csv/tsv file from another csv/tsv file using a key value.
# For example, you have [customerID] in bigdata and would like to delete records in bigdata listed in removallist[customerID].

from os import remove
import pandas as pd

# set removallistcsv/tsv directory
removallist = pd.read_csv('removallistDIR.txt',delimiter='\t', quotechar='"', dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False)

# set big data file to have records removed FROM
bigdata = pd.read_csv('originallistDIR.txt',delimiter='\t', quotechar='"', dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False)

# correlates bigdata to removallist SET KEY VALUE HERE
keyvalue = 'KEYVALUECOLUMNNAME'
records_removed = bigdata[bigdata[keyvalue].isin(removallist[keyvalue])]
output_file = bigdata[~bigdata[keyvalue].isin(removallist[keyvalue])]

# print report in console
print("Length of orignal data: " + str(len(bigdata)))
print("Length records to be removed: " + str(len(removallist)))
print("Records removed: " +  str(len(recordsremoved)))
print("Final result after removes: " + str(len(output_file)))

# outputs a csv file to list out removed records to double check
removed_records = recordsremoved.to_csv('removed_records.txt',sep="\t", index=False, header=True, mode='a')

# outputs the bigdata file with records removed
final_file = output_file.to_csv('final_records.txt',sep="\t", index=False, header=True, mode='a')