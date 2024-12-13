class Database:

    @staticmethod
    def valid_pass(passwd):
        if len(passwd) < 8 or passwd.lower() == passwd or any(char in ".,:;!_*-+()/#¤%&@$^=)" for char in passwd) == False:
            print("Символов в пароле должно быть не менее 8.\nПароль должен содержать хотя бы 1 заглавную букву.\nПароль должен содержать хотя бы 1 спецсимвол.")
            return False
        else:
            return True

    def __init__(self):
        self.data = {'admin' : '123123'}

    def add_user(self, username, password):
        #if self.valid_pass(password):
        self.data[username] = password

class User:


    """ Класс пользователя содержащий атрибуты логин и пароль """
    def __init__(self, username, password, password_confirm, email = ''):
        self.username = username
        if email:
            self.email = email
        if password == password_confirm:
            self.password = password




if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Hi,  choose: \n1 - Login\n2 - Register\n "))
        if choice == 1:
            login = input("Input Login: ")
            password = input("Input pass: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'\nOk! Entered by {login}')
                    break
                else:
                    print("\nInput wrong password!")
            else:
                print("User not found.")
        if choice == 2:
            user = User(input("Input Login: "), password := input("Input pass: "), password2 := input("Confirm pass: "))
            if password != password2:
                print("Passwords don't match try again!")
                continue
            database.add_user(user.username, user.password)
        print(database.data)
