def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи в режиме 'w' с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as f:
        # Проходим по строкам и записываем их
        for i, line in enumerate(strings, start=1):
            # Получаем текущую позицию в файле перед записью строки
            position = f.tell()
            # Записываем строку в файл с добавлением новой строки
            f.write(line + '\n')
            # Сохраняем в словарь: (номер строки, позиция в байтах) -> строка
            strings_positions[(i, position)] = line

    # Возвращаем словарь с результатами
    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Выводим результат
for elem in result.items():
    print(elem)
