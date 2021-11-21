#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerfomance.csv')
print("Мы проверяем гипотезу что результаты экзамена зависят от пола тестируемого")

result_math_f = df[df['gender']=='female']['math score'].mean()
result_math_m = df[df['gender']=='male']['math score'].mean()
result_math_reading_f = df[df['gender']=='female']['reading score'].mean()
result_math_reading_m = df[df['gender']=='male']['reading score'].mean()
result_math_writting_f = df[df['gender']=='female']['writing score'].mean()
result_math_writting_m = df[df['gender']=='male']['writing score'].mean()

print('Результаты по математике:','Девушки', round(result_math_f, 2), 'Парни:', round(result_math_m, 2))
print('Результаты по чтению:','Девушки', round(result_reading_f, 2), 'Парни:', round(result_reading_m, 2))
print('Результаты по письму:','Девушки', round(result_writing_f, 2), 'Парни:', round(result_writing_m, 2))

print('По итогам проверки девушки сильнее в гуманитарных науках парни сильнее в точных науках')

df_f = df[df['gender']=='female']['lunch'].value_counts()
df_m = df[df['gender']=='male']['lunch'].value_counts()
standard_f = df_f['standard']
standard_m = df_m['standard']
free_f = df_f['free/reduced']
free_m = df_m['free/reduced']

print(standard_m, stndard_f, free_f, free_m)
s = pd.Series(data = [standard_f, standard_m, free_f, free_m], index = ['Female_s', 'Male_s',"Female_f",'Male_f'])
s.plot(kind = 'barh')
plt.show()












