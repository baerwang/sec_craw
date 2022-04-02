import time

from lxml import etree

import constant


# 精易论坛 https://bbs.125.la/newatc.htm
class Bbs125(object):
    def parse(self, page, http):
        site_page = 'https://bbs.125.la'
        site = 'https://bbs.125.la/newatc.htm?page=%s' % page
        data = http.request('GET', site, headers=constant.headers).data.decode('utf-8')
        html = etree.HTML(data)
        home = html.xpath('//*[@id="wp"]/ul/li/div[1]/div[1]/a[2]')

        arrays = []

        index = 0

        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        for item in home:
            title = item.text.strip()
            href = item.attrib['href']
            author = item.xpath('//*[@id="wp"]/ul/li/span/a')[index].text
            # print(title, href, author)
            data = http.request('GET', site_page + href, headers=constant.headers).data.decode('utf-8')
            html = etree.HTML(data)
            content = html.xpath('//*[@class="rwd cl"]/div[2]/table')
            if len(content) == 0:
                content = html.xpath('//*[@class="t_fsz"]/table')
            arrays.append({'title': title, 'href': href[1:], 'author': author, 'create_time': create_time,
                           'content': content[0].xpath('string()').strip()})
            index += 1

        return arrays
