import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movies.csv')

print("First three rows:")
print(df.head(3))

print("\nLast three rows:")
print(df.tail(3))

print("\nDataset information:")
print(df.info())

print("\nNull values:")
print(df.isnull().sum())

print("\nRows 41 to 75:")
subset = df.iloc[40:75]
print(subset)

print("\nMovie with the highest number of votes:")
print(df.loc[df['Votes'].idxmax()])

print("\nBoxplots:")
df[['IMDB_Rating', 'Runtime']].plot(kind='box', subplots=True, layout=(1, 2), figsize=(10, 5))
plt.show()

print("\nRelationship between IMDB Rating and Runtime:")
plt.scatter(df['Runtime'], df['IMDB_Rating'])
plt.xlabel('Runtime')
plt.ylabel('IMDB Rating')
plt.title('IMDB Rating vs Runtime')
plt.show()

print("\nDistribution of IMDB Rating and Runtime:")
df[['IMDB_Rating', 'Runtime']].hist(figsize=(10, 5), bins=15)
plt.show()

print("\nCount plot of Rating:")
sns.countplot(x='Rating', data=df)
plt.title('Number of Movies by Rating')
plt.xticks(rotation=45)
plt.show()