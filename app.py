import numpy as np

# Одновимірний масив з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, 200)
print("Початковий масив:\n", array)

# Використовуючи маску --> фільтр всіх додатніх числел
positive_numbers = array[array > 0]
print("Додатні числа:\n", positive_numbers)

#  Всі від’ємні значення замінити на нулі
array[array < 0] = 0
print("Масив після заміни від’ємних значень на 0:\n", array)

# Середнє значення отриманого масиву
mean_value = np.mean(array)
print("Середнє значення:", mean_value)