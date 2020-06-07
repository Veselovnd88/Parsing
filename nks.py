from parse import NksParse

web = 'http://products.naganokeiki.co.jp/'
url = 'http://products.naganokeiki.co.jp/product/?lng=eng'
url2 = 'http://products.naganokeiki.co.jp/product/application.html?lng=eng'
new = NksParse(web)
# new.get_content(url2)
# new.to_json('All kats',new.get_pages())

new.to_json('NKS cardsTrans', new.get_cards('All katsPTrans.json'))
new.to_json('Parsing_NKSPTransducers', new.parse_cards('NKS cardsTrans.json'))