import pandas as pd
import numpy as np

df = pd.read_csv('horse_data.csv', na_values="?")  # импортируем csv-файл, знак "?" воспринимаем как NaN

df = df.iloc[:, [0, 1, 3, 4, 5, 6, 10, 22]]  # выбираем необходимые столбцы
df.columns = ['surgery?', 'Age', 'rectal_temperature', 'pulse',  # Именуем столбцы
              'respiratory_rate', 'temperature_of_extremities',
              'pain', 'outcome']


def stats(column):
    min = df[column].min()
    max = df[column].max()
    range = max - min  # размах
    disp = int(df[column].var().round())  # дисперсия
    mean = int(df[column].mean().round())  # среднее арифметическое
    median = int(df[column].median())  # половина значений - меньше, половина - больше
    mode = int(df[column].mode()[0])  # наиболее часто встречающееся значение в ряду

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    irq = q3 - q1
    lower_bound = q1 - (1.5 * irq)
    upper_bound = q3 + (1.5 * irq)
    outliners = [x for x in df[column] if x < lower_bound or x > upper_bound]  # Выбросы

    print(f'min {column}: {min}, max {column}: {max}, range {column}: {range}, disp {column}: {disp}, '
          f'mean {column}: {mean}, median {column}: {median}, mode {column}: {mode}', sep="\n")
    print(f'Выбросы {column}: {outliners}')
    print('=============')
    return


stats('surgery?')
stats('Age')
stats('rectal_temperature')
stats('pulse')
stats('respiratory_rate')
stats('temperature_of_extremities')
stats('pain')
stats('outcome')

 # Пропуски
print(f'Доля пропусков исходного фрейма: \n{(df.isna().mean() * 100).round(2)}')  # Доля пропусков

df_new = df.copy()
# Заполняем пропуски:
df_new['surgery?'] = df_new['surgery?'].fillna(df.groupby('pain')['surgery?'].transform('median'))
df_new['rectal_temperature'] = df_new['rectal_temperature'].fillna(df.groupby(['temperature_of_extremities', 'pulse'])['rectal_temperature'].transform('median'))
df_new['rectal_temperature'] = df_new['rectal_temperature'].fillna(df['rectal_temperature'].median())
df_new['pulse'] = df_new['pulse'].fillna(df.groupby('Age')['pulse'].transform('median'))
df_new['respiratory_rate'] = df_new['respiratory_rate'].fillna(df['respiratory_rate'].median()) # respiratory_rate заполняем пропуски медианой, т.к. точность исходных данных низкая:
df_new['temperature_of_extremities'] = df_new['temperature_of_extremities'].fillna(df.groupby('rectal_temperature')['temperature_of_extremities'].transform('median'))
df_new['temperature_of_extremities'] = df_new['temperature_of_extremities'].fillna(df['temperature_of_extremities'].median())
df_new['pain'] = df_new['pain'].fillna(df_new.groupby('pulse')['pain'].transform('median'))
df_new['pain'] = df_new['pain'].fillna(df_new['pain'].median())
df_new['outcome'] = df_new['outcome'].fillna(df['outcome'].median())

print(f'Доля пропусков нового фрейма: \n{(df_new.isna().mean() * 100).round(2)}')  # Доля пропусков
print((df_new.isna().mean() * 100).round(2))

#Экспорт в excel
#writer = pd.ExcelWriter('output.xlsx')
#df_new.to_excel(writer)
#writer._save()

# pulse связать с возрастом
# temperature_of_extremities кореллирует с rectal_temperature
# pain медиана по rectal_temperature
# outcome - медиана по возрасту, surgery
