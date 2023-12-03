from datetime import datetime

class User:
    def __init__(self, login, first_name, last_name, age):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.registration_date = datetime.now()

    def display_info(self):
        print(f"Інформація про користувача:\n"
              f"Логін: {self.login}\n"
              f"Ім'я: {self.first_name}\n"
              f"Прізвище: {self.last_name}\n"
              f"Вік: {self.age}\n"
              f"Дата заповнення анкети: {self.registration_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Приклад використання класу User
user1 = User("john_doe", "John", "Doe", 25)
user1.display_info()
