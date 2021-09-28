# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Я', 170],
    ['Отец', 195],
    ['Дядя', 190],
    ['Бабушка', 165],
    ['Мама', 166],
    ['Сестра', 163],
]

my_weight = my_family_height[0][1]
father_weight = my_family_height[1][1]
uncle_weight = my_family_height[2][1]
grandmother_weight = my_family_height[3][1]
mother_weight = my_family_height[4][1]
sister_weight = my_family_height[5][1]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Тест print(f'Рост {my_family_height[1]} см.')

print('Рост Отца - ' + str(my_family_height[1][1]) + ' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

sum_ages = my_weight + father_weight + uncle_weight + grandmother_weight + mother_weight + sister_weight

print('Общий рост моей семьи - ' + str(sum_ages) + ' см')


