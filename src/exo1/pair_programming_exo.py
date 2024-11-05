from abc import ABC, abstractmethod


class Image(ABC):
    def __init__(self, data):
        self._data =data

    @property
    @abstractmethod
    def width(self):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    @property
    @abstractmethod
    def get_pixel(self, x, y):
        pass

    @property
    @abstractmethod
    def set_pixel(self, x, y, color):
        pass


class GrayscaleImage(Image):
    def __init__(self,data):
        super().__init__(data)


    @property
    def width(self):
        return len(self._data[0])

    @property
    def height(self):
        return len(self._data)

    @property
    def get_pixel(self, x, y):
        return self._data[y][x]

    @property
    def set_pixel(self, x, y, color):
        self._data[y][x] = color

data = [[]]
grayscale_image = GrayscaleImage(data)
print(grayscale_image.width)

