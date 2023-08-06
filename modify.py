#import the necessary packages
import pandas as pd

# Read cvs file
df = pd.read_csv('E:\\result.csv')
# extract the first column
df1 = df.iloc[:, 0]
# split each row of the first column
df2 = df1.str.lstrip('_')
df3 = df2.str.split('.t' , expand=True)
df4 = df3.iloc[:, 0]
# save the first column with the rest of the data
dff = pd.concat([df4, df.iloc[:, 1:]], axis=1)
# save the new csv file
dff.to_csv('E:\\xxx.csv', index=False)
