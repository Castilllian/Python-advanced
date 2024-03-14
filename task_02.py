import doctest
import logging

# Настройка логирования
logging.basicConfig(filename='employee_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


# Функция для запуска тестов из командной строки
def run_tests():
    doctest.testmod()


# Функция для обработки аргументов командной строки
def main():
    import argparse

    parser = argparse.ArgumentParser(description='Employee Management System')
    parser.add_argument('--run-tests', action='store_true', help='Run doctests')
    args = parser.parse_args()

    if args.run_tests:
        run_tests()


if __name__ == '__main__':
    main()
