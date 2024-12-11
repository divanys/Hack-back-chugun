import pandas as pd

# Загружаем данные и смотрим на первые несколько строк
df = pd.read_csv("./model/data/dataset_for_nn.csv")
print(df.head())  # Печатаем первые 5 строк
print(df.columns)  # Проверяем, какие столбцы есть в DataFrame