import rembg
import os

# Функция для удаления фона из фотографии с помощью rembg
async def remove_background(filename):
    with open(filename, "rb") as f:
        img = f.read()
    output = rembg.remove(img)
    new_filename = f"rmbkg_{filename}"
    with open(new_filename, "wb") as f:
        f.write(output)
    return new_filename

# Пример использования функции
filename = "example.png"  # имя файла с изображением
new_filename = await remove_background(filename)
print(f"Файл {new_filename} с изображением без фона успешно создан.")