#Задача 4. Вариант 18.
#Напишите программу, которая выводит имя, под которым скрывается Янис Плиекшанс. 
#Дополнительно необходимо вывести область интересов указанной личности, 
#место рождения, годы рождения и смерти (если человек умер), вычислить возраст 
#на данный момент (или момент смерти). Для хранения всех необходимых данных требуется 
#использовать переменные. После вывода информации программа должна дожидаться 
#пока пользователь нажмет Enter для выхода.

#Shamugija L.G.
#13.03.2017

name = 'Янис Плиекшанс более известен, как поэт Райнис.'
place = 'Дунавская волость, Латвия'
year_live = 1865
year_dead = 1929
age = year_dead - year_live
interest = 'Культура'
print(name)
print("Место рождения: ", place)
print("Год рождения: ", year_live, "\nГод смерти:", year_dead)
print("Возраст на момент смерти: ", age)
print("Область интрересов: ", interest)
input("\n\nPress Enter for Exit")

