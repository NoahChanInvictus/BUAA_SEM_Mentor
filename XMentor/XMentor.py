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
    #print html
    url_pool = []
    comp = re.compile(r'<div class="subNav">  <a href="(.*?)"')
    url_pool = comp.findall(html)
    #print url_pool
    return url_pool

def get_subpage_info(url_pool):
    mentor_list = []
    for sub_url in url_pool:
        url = url_base + sub_url
        response = urllib2.urlopen(url)
        html = response.read()
        #print html
        #print type(html)
        comp = re.compile(r'<span style="font-family: 宋体">(.*?)</span></span></strong>')
        names = comp.findall(html)
        for name in names:
            mentor = {}
            name,title = name.split(r'（') 
            title = title.rstrip('）')
            gender = ngender.guess(name)
            mentor['name'] = name
            mentor['gender'] = gender
            mentor['title'] = title
            mentor['department'] = sub_url
            mentor_list.append(mentor)
        print url
        if len(names) != 0:
            continue
        else:
            comp = re.compile(r'<div align="center" style="height: 30px">(.*?)</div>')
            names = comp.findall(html)
            for name in names:
                mentor = {}
                mentor['name'] = name
                gender = ngender.guess(name)
                mentor['gender'] = gender
                mentor['title'] = 'unknown'
                mentor['department'] = sub_url
                mentor_list.append(mentor)
    return mentor_list
        

if __name__ == '__main__':
    url_pool = get_mainpage_info()
    mentors = get_subpage_info(url_pool)
    print mentors
    print len(mentors)
