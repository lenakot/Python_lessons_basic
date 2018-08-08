import os
import shutil

__author__ = "Котова Елена"

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dirs():
    for el in range(1, 10):
        new_dir = 'dir_' + str(el)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

def remove_dirs():
    for el in range(1, 10):
        new_dir = 'dir_' + str(el)
        os.removedirs(new_dir)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def print_dirs():
    all_files = os.listdir()
    for el in all_files:
        if os.path.isdir(el):
            print(el)

## Задача-3:
## Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    copy_file = __file__ + " - copy"
    shutil.copy(__file__, copy_file)

# Для задачи normal. Отображает содержимое папки.
def print_current_dir():
    print(os.getcwd(), ':')
    all_files = os.listdir()
    for el in all_files:
        print(el)
