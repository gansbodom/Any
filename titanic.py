import pandas as pd

titanic = pd.read_csv('https://raw.githubusercontent.com/obulygin/netology_pyda_files/main/titanic.csv')
#titanic.info()
print(titanic.isna().mean() * 100).round(2)