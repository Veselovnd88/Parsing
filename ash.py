from parse import Html, WrongFile, Excel_file
import time


def time_func(func):
    """
    Decoratire for measuring parsing time
    """
    def wrapped(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(str(end - start)+' seconds')
    return wrapped


@time_func
def create_parse(*args):
    pars = Excel_file(*args)


web = 'https://www.ashcroft.eu/en'
URL = 'https://www.ashcroft.eu/en/products/products.html'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0)'
                         ' Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
new = Html(web)
gidnumber = [180, 191]

# TODO Проходка по всему сайту с выгрузкой с созданием разных файлов с заданными именами

