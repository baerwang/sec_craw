from lxml import etree

import constant


# 52破解论坛 https://www.52pojie.cn/forum.php?mod=guide&view=newthread
class PoJie52(object):
    def parse(self, page, http):
        site_page = 'https://www.52pojie.cn/'
        site = 'https://www.52pojie.cn/forum.php?mod=guide&view=newthread&page=%s' % page
        data = http.request('GET', site, headers=constant.headers).data.decode('gbk')
        html = etree.HTML(data)
        home = html.xpath('//*[@id="threadlist"]/div[2]/table/tbody/tr/th/a[1]')

        arrays = []

        for index in range(0, len(home)):
            href = home[index].attrib['href']
            author = html.xpath('//*[@id="threadlist"]/div[2]/table/tbody/tr/td[3]/cite/a/text()')[index]
            create_time = html.xpath('//*[@id="threadlist"]/div[2]/table/tbody/tr/td[3]/em/span/text()')[index]
            # print(home[index].text, href, author, create_time)
            data = http.request('GET', site_page + href, headers=constant.headers).data.decode('gbk')
            content = etree.HTML(data).xpath('//*[@class="pct"]')
            text = ''
            if content:
                text = content[0].xpath('string()').strip()
            arrays.append({'title': home[index].text, 'href': href, 'author': author, 'create_time': create_time,
                           'content': text})

        return arrays
