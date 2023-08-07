import pandas as pd
import numpy as np

df = pd.read_csv('horse_data.csv') # импортируем csv-файл

df1 = df.iloc[:, [1,2,4,5,6,7,11,23]] # выбираем необходимые столбцы
df1.columns = ['surgery?', 'Age', 'rectal temperature', 'pulse',
               'respiratory rate', 'temperature of extremities',
               'pain', 'outcome']

min_age = df1.Age.min()
max_age = df1.Age.max()
range_age = max_age - min_age  # размах
disp_age = int(df1.Age.var().round())
mean_age = int(df1.Age.var().round())
median_age = int(df1.Age.median())  # половина значений - меньше, половина - больше
mode = int(df1.Age.mode()[0])  # наиболее часто встречающееся значение в ряду

#print(f'min_age {min_age},max_age ,range_age range_age,disp_age disp_age,mean_age median_age, mean_age median_age, mode mode')
print(f'min_age: {min_age}, max_age: {max_age}, range_age: {range_age}, disp_age: {disp_age}, '
      f'mean_age: {mean_age}, median_age: {median_age}, mode: {mode}', sep="\n")

print(df1.head())