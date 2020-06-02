from parse import NksParse

url = 'http://products.naganokeiki.co.jp/product/?lng=eng'
new = NksParse()
new.get_content(url)
print(new.get_pages())
