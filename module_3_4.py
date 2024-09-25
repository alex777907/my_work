def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения совпадающих слов
    same_words = []

    # Перебираем слова из other_words
    for word in other_words:
        # Проверяем, содержит ли root_word это слово или наоборот
        if root_word in word or word in root_word:
            same_words.append(word)  # Добавляем слово в список

    # Возвращаем итоговый список совпадающих слов
    return same_words


# Пример вызова функции
result = single_root_words('бег', 'бегун', 'бегемот', 'собака', 'бегать', 'беса')
print(result)  # Ожидаемый вывод: ['бегун', 'бегемот', 'бегать']
