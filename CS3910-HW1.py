 
import pandas as pd

#open the original excel file
df= pd.read_excel('od.xlsx',
                  skiprows=5,
                  skipfooter=7)
#use melt function in pandas to set 'state' as an identifier
df1=pd.melt(df, id_vars=["State"],var_name='year')

#have a list called col1 to store year data
col1=list(df1.year)
#collect year data
col1 = [str(x)[:4] for x in col1]
#assign year data into col1
df1.year=col1
#collect data from row 7 to 57 and store them in col2 list
col2=list(df1.value.iloc[7:57])
#name a column 'Divorce rate'
df1.rename(columns= {'value':'Divorce rate'}, inplace=True)
#sort the state alphabetically and year in ascending order
df1=df1.sort_values(['State','year'])
#add a '%' symbol to divorce rate and replace empty value with a blank space
df1['Divorce rate']=df1['Divorce rate'].apply( lambda x : str(x) + '%').replace('---%','')

#output the data
df1.to_csv('outputdata.csv',na_rep='null', index= False)
