# Дополнительное практическое задание по модулю
import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        else:
            return self.nickname == other

    def __repr__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'{self.title}'

    def __contains__(self, item):
        if isinstance(item, Video):
            return item.title.lower() in self.title.lower()
        else:
            return item.lower() in self.title.lower()

    def __len__(self):
        return self.duration


class UrTube:
    def __init__(self):
        self.current_user = None
        self.videos = []
        self.users = []

    def log_in(self, nickname, password):
        if nickname in self.users:
            user = [user for user in self.users if user == nickname][0]
            password = hash(password)
            if password == user.password:
                print(f'Вход успешен {nickname}')
                self.current_user = user
            else:
                print('Неверный пароль')
        else:
            print('Пользователь не найден')

    def register(self, nickname, password, age):
        if nickname not in self.users:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        self.videos.extend(video)

    def get_videos(self, prompt):
        return [video for video in self.videos if prompt in video]

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        videos = self.get_videos(title)
        if len(videos) == 0:
            return
        if videos[0].adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        for i in range(len(videos[0])+1):
            if i+1 <= len(videos[0]):
                print(i+1, end=" ")
                time.sleep(1)
            else:
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')