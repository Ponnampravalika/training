import pandas as pd
#series
s=pd.Series([10,20,30])
print(s)
#dataframes
data={'name':['aditya','pravalika','krishna'],'age':[26,22,16]}
df=pd.DataFrame(data)
print(df)
#read and write files
df = pd.read_csv('Orders.csv')
df.to_csv('output.csv',index=False)
#excel
df=pd.read_excel('Orders.xlsx')
df.to_excel('output.xlsx',index=False)
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
r=df.describe() 
print(r)
print(df.columns)
#data selection
print(df.columns)
print(df['Quantity'])
df.iloc[0]
df.loc[0,'Quantity']
#filtering rows
print(df[df['Quantity']>22])
print(df[df(['Quantity']>22) & (df['Quantity']<30)])




