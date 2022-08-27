# this tool splits big data in csv/tsv format into smaller tsv/csv files #

import pandas as pd

# set file directories here #
originaldatafile = "./yourbigdatafiledirhere.txt"
new_file_name = "enternewfilenamehere_suffix"
df = pd.read_csv(originaldatafile, delimiter='\t', quotechar='"', quoting=0, dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False)


# this is set to split every 5000 records loc 0 must be the headers
for batch in range(1, (len(df) - 1 )//5000 + 2):

    # iterate through df to select each row up to the last record
    if batch * 5000 > len(df):
        lastrecord = len(df)
    else:
        lastrecord = batch * 5000
    
    batch_new = df.iloc[(batch - 1) * 5000 : lastrecord]
    batch_new['Batch'] = batch
    batch_new['Order'] = range(1,len(batch_new) + 1)
    batch_new.to_csv(new_file_name + str(batch) + '.txt' , index=False, sep='\t')