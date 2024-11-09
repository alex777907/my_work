import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.words_cache = {}  # Кэш для хранения слов из файлов

    def get_all_words(self):
        if self.words_cache:
            return self.words_cache  # Возвращаем из кэша, если уже обрабатывали файлы

        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    text = f.read().lower()
                    # Убираем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation))
                    # Заменяем тире на пробелы (учитываем, что тире может быть без пробела)
                    text = text.replace('-', ' ')  # Заменим тире на пробел
                    text = text.replace(' - ', ' ')  # Заменяем тире с пробелами по бокам
                    # Разбиваем текст на слова
                    words = text.split()

                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")

        self.words_cache = all_words  # Кэшируем результаты
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1  # Позиция по счёту (начинается с 1)
                result[file_name] = position
            else:
                result[file_name] = None  # Если слово не найдено

        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            result[file_name] = count

        return result


# Пример использования
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())  # Все слова
    print(finder.find('text'))  # Позиция слова
    print(finder.count('text'))  # Количество вхождений
