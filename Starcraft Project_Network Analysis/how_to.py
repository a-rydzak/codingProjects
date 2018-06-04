from lxml import html
import requests

#URL pages start here
page0 = requests.get('insert starcraft url here')

#Tree content starts here
tree0= html.fromstring(page0.content)

#Player lists start here
players0 = tree0.xpath('//span[@style="vertical-align:-1px;"]/text()')

#Player scores start here
scores0= tree0.xpath('//div[@style="width:21px"]/text()')


#Test the lengths, only accepted in they are equal
print len(players60)
print len(scores60)