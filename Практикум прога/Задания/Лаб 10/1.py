import os

def count_files(directory):
 count = 0
 for root, dirs, files in os.walk(directory):
  count += len(files)
 return count

# Задайте путь к директории
directory_path = input("/путь/к/директории")

# Подсчитайте количество файлов
num_files = count_files(directory_path)

# Выведите результат
print(f"Количество файлов в директории '{directory_path}': {num_files}")
