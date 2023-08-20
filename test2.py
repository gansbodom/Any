import pandas as pd

# Чтение данных
# При импорте выбираем необходимые для анализа столбцы,именуем, знак "?" воспринимаем как NaN
df = pd.read_csv('horse_data.csv',
                 na_values="?",
                 usecols=[0, 1, 3, 4, 5, 6, 10, 22],
                 names=['surgery?', 'Age', 'rectal_temperature', 'pulse',
                        'respiratory_rate', 'temperature_of_extremities',
                        'pain', 'outcome'])
#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Расчёт базовых статистик
# Для категориальных данных (surgery?, Age, temperature_of_extremities, pain, outcome - категориальные данные)
def cat_base_stats(column):
    mode = int(df[column].mode()[0])  # наиболее часто встречающееся значение в ряду
    uniq_values = df[column].unique()
    print(f' mode {column}: {mode}, uniq_values {column} : {uniq_values}')
    return

# Для непрерывных данных (rectal_temperature, pulse, respiratory_rate - непрерывные)
def cont_base_stats(column):
    min = df[column].min()
    max = df[column].max()
    range = max - min  # размах
    disp = int(df[column].var().round())  # дисперсия
    mean = int(df[column].mean().round())  # среднее арифметическое
    median = int(df[column].median())  # половина значений - меньше, половина - больше


    print(f'min {column}: {min}, max {column}: {max}, range {column}: {range}, disp {column}: {disp},'
          f'mean {column}: {mean}, median {column}: {median}', sep="\n")
    print('=============')
    return


cat_base_stats('surgery?')
cat_base_stats('Age')
cont_base_stats('rectal_temperature')
cont_base_stats('pulse')
cont_base_stats('respiratory_rate')
cat_base_stats('temperature_of_extremities')
cat_base_stats('pain')
cat_base_stats('outcome')


# Расчёт дополнительных статистик
def add_stats(column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    irq = q3 - q1
    lower_bound = q1 - (1.5 * irq)
    upper_bound = q3 + (1.5 * irq)
    outliners = [x for x in df[column] if x < lower_bound or x > upper_bound]  # Выбросы
    print(f'Выбросы {column}: {outliners}')
    print('=============')
    return


add_stats('rectal_temperature')
add_stats('pulse')
add_stats('respiratory_rate')
