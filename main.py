def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Приводим корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Перебираем все другие слова
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержится ли одно слово в другом или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words


# Пример вызова функции
result = single_root_words('Able', 'Disablement', 'Test', 'able', 'AbLe')
print(result)  # Ожидаемый вывод: ['Disablement', 'able', 'AbLe']
