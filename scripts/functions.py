import pygame
import os


def load_image(*paths):
    """Загружает картинку"""
    # Получаем полный путь к картинке
    path = os.path.join(*paths)

    # Загружаем картинку и конвертируем её
    image = pygame.image.load(path).convert()
    # Делаем чёрный цвет прозрачным
    image.set_colorkey((0, 0, 0))

    # Возвращаем картинку из функции
    return image
