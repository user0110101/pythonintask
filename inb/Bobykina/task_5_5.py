#Задача 5. Вариант 5.
#Напишите программу, которая бы при запуске случайным образом отображала название одного из восьми соборов Московского кремля.

#Bobykina D.A.
#14.03.2017
import random

print("Программа случайным образом отображает название одного из возьми соборов Московского Кремля.")
sobor = ("Колокольня Ивана Великого", 
"Успенский собор",
"Благовещенский собор",
"Архангельский собор",
"Храм Положения ризы Божией Матери во Влахерне",
"Патриарший дворец и собор Двенадцати апостолов",
"Верхоспасский собор",
"Церковь Рождества Богородицы на Сенях")
print("Случайный собор - ", sobor[random.randint(0, len(sobor) - 1)])
input("Введите Enter для выхода")
