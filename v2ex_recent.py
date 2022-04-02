import time
from lxml import etree

import constant


# v2ex论坛 https://www.v2ex.com/recent
class V2exRecent(object):
    def parse(self, page, http):
        site_page = 'https://www.v2ex.com'
        site = 'https://www.v2ex.com/recent?p=%s' % page
        data = http.request('GET', site, headers=constant.headers).data.decode('utf-8')

        html = etree.HTML(data)
        home = html.xpath('//span[@class="item_title"]/a')
        authors = html.xpath('//span[@class="topic_info"]')

        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        arrays = []
        index = 0

        for item in home:
            title = item.text
            href = item.attrib['href']
            author = authors[index].find('strong')[0].text
            # print(title, href, author)
            data = http.request('GET', site_page + href, headers=constant.headers).data.decode('utf-8')
            html = etree.HTML(data)
            content = html.xpath('//*[@class="topic_content"]')
            arrays.append({'title': title, 'href': href, 'author': author, 'create_time': create_time,
                           'content': content[0].xpath('string()').strip()})
            index += 1

        return arrays
