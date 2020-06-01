from parse import Html, WrongFile, ExcelFile
import time


def time_func(func):
    """
    Decoratire for measuring parsing time
    """

    def wrapped(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(str(end - start) + ' seconds')

    return wrapped


@time_func
def create_parse(*args):
    pars = ExcelFile(*args)


web = 'https://www.ashcroft.eu/en'
URL = 'https://www.ashcroft.eu/en/products/products.html'
URL1 = 'https://www.ashcroft.eu/en/products/products.html?gid=48'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0)'
                         ' Gecko/20100101 Firefox/71.0', 'accept': '*/*'}

#  Блок списков со страницами
pgpages = [34, 62, 38, 36, 57, 35, 37]
switchespages = [42, 43, 44]
temppages = [39, 40, 65, 66]
transducerspages = [73, 45, 70, 46, 47]
testpages = [50, 49, 51, 48]
sealpages = [53, 64, 54, 61, 67, 68, 55]
wellspage = [7]
accespage = [71, 58, 59, 60, 56]

new = Html(web)
thermowells_numbers = [321, 322, 323, 324, 325, 326]


def parse_fullpage(numbers, url, obj):
    """
    Функция принимает список с номерами страниц со списками продукции,
    ссылку products
    и созданный объект класса Html
    Для термокарманов не работает
    :param numbers: list
    :param url: str
    :param obj: instance
    :return:
    """
    for i in numbers:
        web = url + '?gid=' + str(i)
        obj.get_content(web)
        create_parse(obj.get_numbers(), obj.title_page(), new, 0, URL)


# create_parse(gidnumber,'Process',new,0,URL)
# create_parse(gidnumber, 'Thermowells', new,0, URL)
parse_fullpage(wellspage, URL, new)
