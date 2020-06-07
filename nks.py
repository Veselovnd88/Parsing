from parse import NksParse

web = 'http://products.naganokeiki.co.jp/'
url = 'http://products.naganokeiki.co.jp/product/?lng=eng'
url2 = 'http://products.naganokeiki.co.jp/product/application.html?lng=eng'
new = NksParse(web)
# new.get_content(url2)
# new.to_json('All kats',new.get_pages())

new.to_json('NKS cardsSwitch', new.get_cards('All katsPSwitch.json'))
new.to_json('Parsing_NKSPSwitch', new.parse_cards('NKS cardsSwitch.json'))