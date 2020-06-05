"""

@author: Mikaeel

"""

corpus = '<html><head></head><body><h1>Paragraph Heading</h1><p>This is some text. <a href="">The original price was $500 but now only USD250 </a> This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is <em>some text.</em> <strong>This is some text.</strong> This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. This is some text. </p></body></html>'

print('Raw data: ', corpus)

import re

tags = re.compile(r'<.*?>')
corpus = tags.sub('', corpus)

prices = re.compile(r'(USD|\$)[0-9]+')
corpus = prices.sub('', corpus)

print('normalized data: ', corpus)