# -*- coding: utf-8 -*-
import re
import urllib2
import ngender

url_base = 'http://sem.buaa.edu.cn/szdw/'

#print ngender.guess('赵本山')
def get_mainpage_info():
    
    url = url_base + 'jsbd.htm'
    response = urllib2.urlopen(url)
    html = response.read()
    print html
    url_pool = []
    comp = re.compile(r'<div class="subNav">  <a href="(.*?)"')
    url_pool = comp.findall(html)
    print url_pool
    return url_pool

def get_subpage_info(url_pool):
    for sub_url in url_pool:
        url = url_base + sub_url
        response = urllib2.urlopen(url)
        html = response.read().decode('utf-8')
        #print html
        comp = re.compile(r'<span style="font-family: 宋体">(.*?)</span></span></strong>')
        names = comp.findall(html)
        #for name in names:
            #print name.split('(')


        print len(names)
        return 0

if __name__ == '__main__':
    url_pool = get_mainpage_info()
    get_subpage_info(url_pool)
