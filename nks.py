from parse import NksParse

web = 'http://products.naganokeiki.co.jp/'
url = 'http://products.naganokeiki.co.jp/product/?lng=eng'
new = NksParse(web)
new.get_content(url)


new.to_json('NKS cards',new.get_cards())
