import logging
import argparse

# Настройка логирования
logging.basicConfig(filename='archive_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidTextError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid text: {self.text}. Text should be a non-empty string.'


class InvalidNumberError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number: {self.number}. Number should be a positive integer or float.'


class Archive:
    """Документация для класса Архив"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        if not isinstance(text, str) or len(text.strip()) == 0:
            logging.error(f'InvalidTextError: {text}')
            raise InvalidTextError(text)
        if not (isinstance(number, int) or isinstance(number, float)) or number <= 0:
            logging.error(f'InvalidNumberError: {number}')
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


# Функция для запуска из командной строки
def main():
    parser = argparse.ArgumentParser(description='Archive Management System')
    parser.add_argument('--text', type=str, required=True, help='Text for archive')
    parser.add_argument('--number', type=float, required=True, help='Number for archive')
    args = parser.parse_args()

    try:
        archive = Archive(args.text, args.number)
        print(archive)
    except (InvalidTextError, InvalidNumberError) as e:
        print(e)


if __name__ == '__main__':
    main()
