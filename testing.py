import datetime
import os
def create_path():
    """Создаст путь для файла эксель, ,диск С/ДДММГГ-Parse """ # TODO
    creation_time = str(datetime.datetime.now())[:10]
    basic_path = 'C:\ParseProject'
    filepath = os.path.join(basic_path,creation_time)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    return filepath

print(create_path())
