from time import sleep

class User:

    def __init__(self, nick, password, age):
        self.nickname = nick
        self.password = hash(password)
        self.age = age

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False ):
            self.title = title
            self.duration = duration
            self.time_now = time_now
            self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = ''

    def log_in(self,nickname, password ):
        nickname = input("Input Nickname: ")
        password = input("Input pass: ")
        if nickname in self.users:
            if password == self.users[login]:
                print(f'\nOk! Entered by {login}')

            else:
                print("\nInput wrong password!")
        else:
            print("User not found.")

    def register(self,nickname, password, age):
        for name in self.users:
            if name == nickname:
                print(f'Пользователь {nickname} уже существует"')
            else:
                self.users.append(nickname)
    def logout(self):
        self.current_user = None

    def add(self, *args):
        pass

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

print(vars(v2))
