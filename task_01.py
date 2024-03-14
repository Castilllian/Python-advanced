import logging
import argparse

# Configure logging
logging.basicConfig(filename='rectangle.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            msg = f'Ширина должна быть положительной, а не {width}'
            logging.error(msg)
            raise NegativeValueError(msg)
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                msg = f'Высота должна быть положительной, а не {height}'
                logging.error(msg)
                raise NegativeValueError(msg)
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            msg = f'Ширина должна быть положительной, а не {value}'
            logging.error(msg)
            raise NegativeValueError(msg)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            msg = f'Высота должна быть положительной, а не {value}'
            logging.error(msg)
            raise NegativeValueError(msg)

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

def main():
    parser = argparse.ArgumentParser(description='Perform operations on rectangles.')
    parser.add_argument('width1', type=float, help='width of first rectangle')
    parser.add_argument('height1', type=float, nargs='?', default=None, help='height of first rectangle')
    parser.add_argument('width2', type=float, help='width of second rectangle')
    parser.add_argument('height2', type=float, nargs='?', default=None, help='height of second rectangle')

    args = parser.parse_args()

    try:
        r1 = Rectangle(args.width1, args.height1)
        r2 = Rectangle(args.width2, args.height2)

        r3 = r1 + r2
        r4 = r1 - r2

        print(f"Perimeter of r1 + r2: {r3.perimeter()}")
        print(f"Area of r1 + r2: {r3.area()}")

        print(f"Perimeter of r1 - r2: {r4.perimeter()}")
        print(f"Area of r1 - r2: {r4.area()}")

    except NegativeValueError as e:
        print(e)

if __name__ == "__main__":
    main()
