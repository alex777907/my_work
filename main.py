import os
import time

# 1. Определение целевого каталога
# Путь к каталогу можно изменить на нужный. Текущий каталог обозначается точкой "."
directory = "."

# 2. Обход каталога с помощью os.walk
for root, dirs, files in os.walk(directory):
    # 3. Обход каждого файла в текущем каталоге
    for file in files:
        # 4. Формирование полного пути к файлу
        filepath = os.path.join(root, file)

        try:
            # 5. Получение времени последнего изменения файла
            filetime = os.path.getmtime(filepath)
            # Форматирование времени в удобочитаемый вид
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            # 6. Получение размера файла в байтах
            filesize = os.path.getsize(filepath)

            # 7. Получение родительской директории файла
            parent_dir = os.path.dirname(filepath)

            # 8. Вывод информации о файле
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

        except Exception as e:
            # Обработка возможных ошибок, например, если файл недоступен
            print(f'Не удалось получить информацию о файле: {filepath}. Ошибка: {e}')
