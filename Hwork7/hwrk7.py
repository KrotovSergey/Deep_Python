# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало

from pathlib import Path

from hwrk7_2 import *


def group_rename_files(new_name: str, ext_renamed: str, /, count_dig: int = 3, ext_new: str = None,
                       saved_range: range = (3, 6), path: str = None) -> int:
    if ext_new is None:
        ext_new = ext_renamed

    work_path = Path.cwd() if path is None else Path(path)
    count_renamed = 0
    for p in work_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            number = str(count_renamed).zfill(count_dig)
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{number}{ext_new}"
            p.rename(Path(p.parent, file_name))
            count_renamed += 1

    return count_renamed


makefiles(mp3=5, txt=4, wav=6)

if __name__ == '__main__':
    print("файлов переименовано: ", group_rename_files("new", ".jpg", ext_new=".png", count_dig=4))
