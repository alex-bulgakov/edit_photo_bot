import rembg
import os


# Функция для удаления фона из фотографии с помощью rembg
def remove_background(img):
    return rembg.remove(img)
