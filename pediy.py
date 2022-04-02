from lxml import etree

import constant


# 看雪论坛 https://bbs.pediy.com/new-tid.htm
class Pediy(object):
    def parse(self, page, http):
        site_page = 'https://bbs.pediy.com/'
        site = 'https://bbs.pediy.com/new-tid-%s.htm' % page
        data = http.request('GET', site, headers=constant.headers).data.decode('utf-8')
        html = etree.HTML(data)
        home = html.xpath('//td/div[1]/a[2]')

        arrays = []

        for item in home:
            title = item.text
            href = item.attrib['href']
            author = item.xpath('//td/div[2]/div[1]/a')[0].text
            create_time = item.xpath('//td/div[2]/div[1]/span')[0].text
            # print(title, href, author, create_time)
            data = http.request('GET', site_page + href, headers=constant.headers).data.decode('utf-8')
            html = etree.HTML(data)
            content = html.xpath('//*[@class="message "]')
            arrays.append({'title': title, 'href': href, 'author': author, 'create_time': create_time,
                           'content': content[0].xpath('string()').strip()})

        return arrays
