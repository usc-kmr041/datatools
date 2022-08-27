# this tool turns a list into a dictionary. For example, customer records merged with payment transactions using a key value. #

import pandas as pd
import json

# set cleaned csv/tsv files to be manipulated
original_file = './yourcustomerrecordsDIR.csv'
sub_file = './transactionaldataDIR.csv'
output_file = 'finaloutput.json'

# load files onto dataframes
origin = pd.read_csv(original_file, delimiter='\t', quotechar='"', quoting=0, dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False, encoding='cp1252')
sub_file = pd.read_csv(sub_file, delimiter='\t', quotechar='"', quoting=0, dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False, encoding='cp1252')

# null json object container for output
output_json = []

# this iterates over each row in origin file
for index, row in origin.iterrows():
	new_record = row.to_dict()
	# set key value in the two dataframes
	matching_records = sub_file.loc[sub_file['setkeyvaluepairhere'] == row['setkeyvaluepairhere']]
	# get the list of fields to output for each transaction. This will exclude specific fields and include the rest
	trans_field_list = matching_records.columns.difference(['ContactID'], sort=False)
	#change name here
	new_record['sub_file'] = matching_records[trans_field_list].to_dict('newrecordname')
	output_json.append(new_record)


with open(output_file, 'w') as f:
	f.write(json.dumps(output_json, default=str))

print('Done')