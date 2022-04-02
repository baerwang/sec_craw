import json

from lxml import etree

import constant


# 90sec 账号审核 https://forum.90sec.com/c/account/11
class Sec9011(object):
    def parse(self, page, http):
        site_page = 'https://forum.90sec.com/t/topic/'
        site = 'https://forum.90sec.com/c/account/11.json?page=%s' % page
        data = http.request('GET', site, headers=constant.headers).data.decode('utf-8')

        data = json.loads(data)['topic_list']['topics']
        arrays = []

        for item in data:
            href = site_page + str(item['id'])
            title = item['title']
            create_time = item['created_at']
            # print(title, href, create_time)

            resp = http.request('GET', href, headers=constant.headers).data.decode('utf-8')
            html = etree.HTML(resp)
            author = html.xpath('//span[@class="creator"]/a/span')[0].text
            content = html.xpath('//*[@itemprop="articleBody"]')
            arrays.append({'title': title, 'href': href, 'author': author, 'create_time': create_time,
                           'content': content[0].xpath('string()').strip()})

        return arrays
