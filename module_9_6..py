def all_variants(text):
    # Два вложенных цикла для генерации всех подпоследовательностей
    for start in range(len(text)):  # Перебираем все возможные начальные индексы
        for end in range(start + 1, len(text) + 1):  # Перебираем все возможные конечные индексы
            yield text[start:end]  # Возвращаем подстроку от start до end

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)
