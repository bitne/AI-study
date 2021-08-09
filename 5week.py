%matplotlib inline
import pandas as pd
import seaborn as sns

df=pd.read_csv('insurance.csv')
sns.violinplot(data=df, x='smoker',y='charges')
sns.violinplot(data=df, x='children',y='charges')
sns.violinplot(data=df, x='region',y='charges')
corr=df.corr()
corr['charges']
df.plot(kind='scatter',x='age',y='charges')
smoker= df[(df['smoker']=='yes')& (df['bmi']>=30) &((df['bmi']<=50))]
smoker.plot(kind='scatter',x='age',y='charges')