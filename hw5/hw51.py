import pandas as pd

#don't show copy warning
pd.options.mode.chained_assignment = None

#read in the data to pandas dataframe
df=pd.read_excel('origin.xls',
               header=0,
               na_values='null',
               index_col=None)
#covert null values into a list
null_list = df.index[df.isnull().any(axis=1) == True].tolist()

#print all null values
def printmissing(df,name):
    print (name+":\n",df.iloc[null_list], '\n')
printmissing(df,"original null values")
#print a summary of all the null values
print("number of null values in the dataframe:\n",df.isna().sum(), '\n')


#get a new dataframe with only values for Colorado
co_fix=df.loc[df['State']=='Colorado']
#use LOCF method to fill the missing value
co_fix.fillna(method='bfill',inplace=True)
#fill the values to original dataframe
df=df.fillna(co_fix)


#get a new dataframe with only values for Indiana                
indiana_fix=df.loc[df['State'] == 'Indiana']
#drop all of the columns except for divorce rate
indiana_fix.drop(['Marriage_Rate','Year'],axis=1,inplace=True)
#calculate the mean divorce rate for a subset of data containing only Ohio and Illinois.
mean_div = df['Divorce_Rate'].loc[df['State'].isin(['Ohio','Illinois'])].mean()
#set all of the divorce rates in indiana_fix to be the mean of both Ohio and Illinois
indiana_fix['Divorce_Rate']=mean_div
#fill the values to original dataframe
df.fillna(indiana_fix,inplace=True)
#printmissing(df,"fixed Indiana")

#get a new dataframe with only values for Louisiana                
la_fix=df.loc[df['State'] == 'Louisiana']
#drop all of the columns except for divorce rate
la_fix.drop(['Marriage_Rate','Year'],axis=1,inplace=True)
#calculate the mean divorce rate for a subset of data containing only Ohio and Iowa.
mean_div = df['Divorce_Rate'].loc[df['State'].isin(['Ohio','Iowa'])].mean()
#set all of the divorce rates in indiana_fix to be the mean of both Ohio and Iowa
la_fix['Divorce_Rate']=mean_div
#fill the values to original dataframe
df.fillna(la_fix,inplace=True)
#printmissing(df,"fixed Louisiana")



#use forward fill method for the rest states which are missing values
ffillfix=df.fillna(method='ffill')
#fill the values to original dataframe
df=df.fillna(ffillfix)
#printmissing(df,'sss')

#output to csv file
df.to_csv('fixed.csv',index=False)
