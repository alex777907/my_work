import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    text = f.read().lower()
                    # Убираем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation + ' -'))
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")

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
    print(finder.find('TEXT'))  # Позиция слова
    print(finder.count('teXT'))  # Количество вхождений
