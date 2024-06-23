# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
import numpy as np
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
# print(pd.get_dummies(data))

unique__values = data["whoAmI"].unique() # Получаем уникальные значения из столбца "whoAmI"
one__hot__date = pd.DataFrame() # Создаем пустой DataFrame
# Для каждого уникального значения создаем новый столбец и заполняем его значениями 0 или 1
for value in unique__values:
    one__hot__date[value] = (data["whoAmI"] == value).astype(int)
print(one__hot__date.head()) 