#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
#Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


import os.path
def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)
path = "c:/Users/Vladislav/Desktop/deep_to_python/test.txt"
my_st = parse_path(path)
print("The output tuple", my_st)