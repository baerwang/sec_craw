from urllib3 import ProxyManager

import bbs125
import pediy
import pojie52
import sec90
import v2ex_recent


def executor(obj, index, page):
    # proxy support htt or https
    # default_headers = make_headers(proxy_basic_auth='myusername:mypassword')
    http = ProxyManager("http://127.0.0.1:7890", num_pools=page)

    # standard http
    # http = urllib3.PoolManager(num_pools=page)
    for num in range(index, page):
        print(obj.parse(num, http))


# learn https://blog.csdn.net/xunxue1523/article/details/104584886
if __name__ == '__main__':
    info = {'看雪': '1', '52破解论坛': '2', '精易论坛': '3', 'V2ex_Recent': '4', '90sec_11': '5'}

    if info.__contains__('V2ex_Recent'):
        craw = {'1': pediy.Pediy(), '2': pojie52.PoJie52(), '3': bbs125.Bbs125(), '4': v2ex_recent.V2exRecent(),
                '5': sec90.Sec9011()}
        executor(craw[info['V2ex_Recent']], 1, 2)
