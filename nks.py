from parse import  Html, NksParse

url = 'http://products.naganokeiki.co.jp/product/?lng=eng'
new = NksParse()
new.get_content(url)
new.get_pages()
