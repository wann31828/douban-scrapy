# -*- coding: utf-8 -*-

import random

from fake_useragent import UserAgent
from scrapyspider.settings import PROXY_LIST

class RandomUserAgentMiddlware(object):
   
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        #读取在settings文件中的配置，来决定ua采用哪个方法，默认是random，也可是ie、Firefox等等，参考前面的使用方法。
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    #更换用户代理逻辑在此方法中
    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        print  (get_ua())
        request.headers.setdefault('User-Agent', get_ua())

class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        # request.meta['proxy'] = "https://175.9.77.240:80"
        request.meta['proxy'] = random.choice(PROXY_LIST)
