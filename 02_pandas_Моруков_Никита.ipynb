#1.1 В файлах recipes_sample.csv и reviews_sample.csv находится информация об рецептах блюд и отзывах на эти рецепты 
#соответственно. Загрузите данные из файлов в виде pd.DataFrame с названиями recipes и reviews. Обратите внимание на 
#корректное считывание столбца с индексами в таблице reviews (безымянный столбец).
#2.1 Преобразуйте столбец submitted из таблицы recipes в формат времени. Модифицируйте решение задачи 1.1 так, чтобы считать столбец сразу в нужном формате.

import pandas as pd
import numpy as np
recipes = pd.read_csv('recipes_sample.csv', parse_dates=['submitted'])
reviews = pd.read_csv('reviews_sample.csv', index_col=[0])
recipes[:3]


#1.2 Для каждой из таблиц выведите основные параметры:

 #   количество точек данных (строк);
 #   количество столбцов;
 #   тип данных каждого столбца.

print('Количество строк для первой таблицы =',len(recipes.axes[0]),
      '\nКоличество столбцов для первой таблицы =', len(recipes.axes[1]))
for i in range(0,len(recipes.axes[1])):
    print('Тип данных для',i+1, 'столбца:',type(recipes.iloc[0, i]))

print('Количество строк для второй таблицы =',len(reviews.axes[0]),
      '\nКоличество столбцов для второй таблицы =', len(reviews.axes[1]))
for i in range(0,len(reviews.axes[1])):
    print('Тип данных для',i+1, 'столбца:',type(reviews.iloc[0,i]))


#1.3 Исследуйте, в каких столбцах таблиц содержатся пропуски. Посчитайте долю строк, содержащих пропуски, в отношении к общему количеству строк.

null_rows_total1 = recipes.shape[0] - recipes.dropna().shape[0]    
print('Количество пропусков в каждом столбце первой таблицы:\n', recipes.isna().sum())
print('Доля строк, содержащих пропуски: ', (null_rows_total1/len(recipes.axes[0]))*100,'%',sep='' )

null_rows_total2 = reviews.shape[0] - reviews.dropna().shape[0]
print('Количество пропусков в каждом столбце второй таблицы:\n', reviews.isna().sum())
print('Доля строк, содержащих пропуски: ', (null_rows_total2/len(reviews.axes[0]))*100,'%',sep='' )


#1.4 Рассчитайте среднее значение для каждого из числовых столбцов (где это имеет смысл).

print('Среднее значение для столбца minutes: ', recipes['minutes'].mean(), 
      '\nСреднее значение для столбца n_steps: ', recipes['n_steps'].mean(), 
      '\nСреднее значение для столбца n_ingredients: ', recipes['n_ingredients'].mean())

print('Среднее значение для столбца rating: ', reviews['rating'].mean())


#1.5 Создайте серию из 10 случайных названий рецептов.

ten_recipes = pd.Series(recipes['name'].sample(n = 10))
ten_recipes


#1.6 Измените индекс в таблице reviews, пронумеровав строки, начиная с нуля.

reviews.reset_index()


#1.7 Выведите информацию о рецептах, время выполнения которых не больше 20 минут и кол-во ингредиентов в которых не больше 5.

recipes[(recipes.minutes < 21) & (recipes.n_ingredients < 6)]


#2.2 Выведите информацию о рецептах, добавленных в датасет не позже 2010 года.

recipes[recipes['submitted']>='2010-01-01']


#3.1 Добавьте в таблицу recipes столбец description_length, в котором хранится длина описания рецепта из столбца description.

recipes['description_length']  = recipes['description'].str.len()


#3.2 Измените название каждого рецепта в таблице recipes таким образом, чтобы каждое слово в названии начиналось с прописной буквы.

recipes['name'] = recipes['name'].str.capitalize()


#3.3 Добавьте в таблицу recipes столбец name_word_count, в котором хранится количество слов из названии рецепта (считайте, что слова в названии 
#разделяются только пробелами). Обратите внимание, что между словами может располагаться несколько пробелов подряд.

recipes['name_word_count'] = [len(x.split()) for x in recipes['name'].tolist()]


#4.1 Посчитайте количество рецептов, представленных каждым из участников (contributor_id). Какой участник добавил максимальное кол-во рецептов?

c = recipes.groupby("contributor_id").size()
print('Количество рецептов, представленных каждым из участников', c, 
      '\nУчастник, который добавил наибольшее кол-во рецептов: ', 
      c[c == c.max()].index[0])


#4.2 Посчитайте средний рейтинг к каждому из рецептов. Для скольких рецептов отсутствуют отзывы? Обратите внимание, что отзыв с нулевым рейтингом или не 
#с нулевым рейтингом или не заполненным текстовым описанием не считается отсутствующим.
print('Кол-во рецептов, для которых отсутствуют отзывы', 
      len(recipes.groupby('name').size()) - len(reviews.groupby('recipe_id').size()))
reviews.groupby('recipe_id').mean('rating').drop('user_id', axis=1)


#4.3 Посчитайте количество рецептов с разбивкой по годам создания.

recipes.groupby(recipes.submitted.dt.year).size()


#5.1 При помощи объединения таблиц, создайте DataFrame, состоящий из четырех столбцов: id, name, user_id, rating. Рецепты, на 
#которые не оставлен ни один отзыв, должны отсутствовать в полученной таблице. Подтвердите правильность работы вашего кода, 
#выбрав рецепт, не имеющий отзывов, и попытавшись найти строку, соответствующую этому рецепту, в полученном DataFrame.

df = recipes[['id','name']].copy()
df5_1 = df.merge(reviews[['user_id','rating']], left_on='id', right_on='user_id')


#5.2 При помощи объединения таблиц и группировок, создайте DataFrame, состоящий из трех столбцов: recipe_id, name, 
#review_count, где столбец review_count содержит кол-во отзывов, оставленных на рецепт recipe_id. У рецептов, на которые не 
#оставлен ни один отзыв, в столбце review_count должен быть указан 0. Подтвердите правильность работы вашего кода, выбрав 
#рецепт, не имеющий отзывов, и найдя строку, соответствующую этому рецепту, в полученном DataFrame.

df = recipes[['recipe_id','name']].copy()


#5.3. Выясните, рецепты, добавленные в каком году, имеют наименьший средний рейтинг?

df = recipes[['id','name']].copy()
df = df.merge(reviews[['recipe_id', 'rating', 'date']], right_on='recipe_id', left_on='id')
df = df.drop(['id', 'name', 'recipe_id'], axis=1)
df.date = pd.DatetimeIndex(df.date).to_period("Y")
df.groupby('date').mean().sort_values('rating')


#6.1 Отсортируйте таблицу в порядке убывания величины столбца name_word_count и сохраните результаты выполнения заданий 3.1-3.3 в csv файл. 

recipes = recipes.sort_values(by=['name_word_count'], ascending=False)
recipes.to_csv("my_data.csv", index=True)


#6.2 Воспользовавшись pd.ExcelWriter, cохраните результаты 5.1 и 5.2 в файл: на лист с названием Рецепты с оценками сохраните 
#результаты выполнения 5.1; на лист с названием Количество отзывов по рецептам сохраните результаты выполнения 5.2.

with pd.ExcelWriter("res.xlsx") as writer:
    df5_1.to_excel(writer, sheet_name="Рецепты с оценками")  
    df5_2.to_excel(writer, sheet_name="Количество отзывов по рецептам")
