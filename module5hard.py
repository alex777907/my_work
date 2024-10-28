import hashlib
import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password: str) -> int:
        # Хэшируем пароль с использованием SHA-256 и преобразуем в целое число
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __repr__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration  # в секундах
        self.time_now = 0  # начальное время показа
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь

    def log_in(self, nickname: str, password: str):
        hashed_password = self._hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь '{nickname}' успешно вошёл в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname: str, password: str, age: int):
        # Проверяем, существует ли пользователь с таким nickname
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        # Создаем нового пользователя и добавляем в список
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Входим автоматически после регистрации
        print(f"Пользователь '{nickname}' успешно зарегистрирован и вошёл в систему.")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь '{self.current_user.nickname}' вышел из системы.")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует. Пропуск.")

    def get_videos(self, search_word: str):
        search_word_lower = search_word.lower()
        matching_videos = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return matching_videos

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Ищем точное совпадение названия видео
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            # Точное совпадение не найдено
            print(f"Видео '{title}' не найдено.")
            return

        # Проверяем возрастные ограничения
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинается просмотр видео '{video.title}'")
        video.time_now = 0  # Сбрасываем время просмотра

        for second in range(1, video.duration + 1):
            print(f"Просмотр на {second} секунде...")
            time.sleep(0.1)  # Уменьшил время сна для ускорения демонстрации
            video.time_now = second

        print("Конец видео")

        video.time_now = 0  # Сбрасываем время просмотра после завершения

    def _hash_password(self, password: str) -> int:
        # Вспомогательный метод для хэширования пароля
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __repr__(self):
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"


# Код для проверки:
if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 5)  # Уменьшил длительность для быстрой проверки
    v2 = Video('Для чего девушкам парень программист?', 3, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print("Поиск 'лучший':", ur.get_videos('лучший'))
    print("Поиск 'ПРОГ':", ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print("Текущий пользователь:", ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
