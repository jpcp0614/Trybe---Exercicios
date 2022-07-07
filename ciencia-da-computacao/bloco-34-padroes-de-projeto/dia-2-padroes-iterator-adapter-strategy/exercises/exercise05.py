'''
Você tem a implementação de uma classe capaz renderizar imagens
através de uma interface que utiliza o método draw.
Porém, no momento ela só suporta formato PNG e você também precisa
ser capaz de renderizar imagens em SVG. Altere o código,
sem modificar a classe SvgImage, para que isso seja possível.

DICA:
Se você garantir que a imagem SVG seja renderizada utilizando a
mesma interface que a imagem PNG, a imagem se tornará compatível.
'''

from abc import ABC, abstractmethod


class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class PngImage(PngInterface):
    def __init__(self, png_path):
        self.png_path = png_path
        self.format = "raster"

    def draw(self):
        print(f"Drawing PNG {self.png_path} with {self.format}")


class SvgImage:
    def __init__(self, svg_path):
        self.svg_path = svg_path
        self.format = "vector"

    def get_image(self):
        return f"SVG {self.svg_path} with {self.format}"


class SvgImageAdapter(PngInterface):
    def __init__(self, svg_image):
        self.svg_image = svg_image

    def draw(self):
        print(f'Drawing SVG {self.svg_image.get_image()}')


imageSVG = SvgImage('exercicio05.svg')

SvgImageAdapter(imageSVG).draw()
