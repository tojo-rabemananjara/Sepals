# Import pandas with alias
import pandas as pd, numpy as np

# Assign the dataset url as a variable
url = "https://raw.githubusercontent.com/shrikant-temburwar/Iris-Dataset/master/Iris.csv"
 
# Define the column names of dataset as a list
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
 
# Use read_csv to read in data as a pandas dataframe
df = pd.read_csv(url, header = 0, names=columns)

df['sepal_length'] = df['sepal_length'].astype(float)
df['sepal_width'] = df['sepal_width'].astype(float)
df['petal_length'] = df['petal_length'].astype(float)
df['petal_width'] = df['petal_width'].astype(float)

sepal_lengths, sepal_widths = df['sepal_length'], df['sepal_width']
petal_lengths, petal_widths = df['petal_length'], df['petal_width']

# Check head of dataframe
print(df.head())
print(sorted(sepal_lengths, reverse=True))

print("Average sepal length is: {} cm".format(round(np.average(sepal_lengths),2)))
print("Average sepal width is: {} cm".format(round(np.average(sepal_widths),2)))
print("Average petal length is: {} cm".format(round(np.average(petal_lengths),2)))
print("Average petal width is: {} cm".format(round(np.average(petal_widths),2)))