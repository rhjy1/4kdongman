import urllib.request
import re
import os
import urllib
import requests

def main():
    main_index_html = 'http://pic.netbian.com/4kdongman/'
    index_html = main_index_html

    #range(开始页数,结束页数)
    for index in range(1,146):
        if(index != 1):
            index_html = main_index_html + "index_" + str(index) + ".html"
            print("index_html = " + index_html)
            page(index_html)

def page(index_html):
    main_addr = "http://pic.netbian.com/"
    html_data = get_html(index_html)
    pat = '/tupian/(.*?).html'
    xiao_tu_pian = get_addr(pat, html_data)
    for xtp in xiao_tu_pian:
        xtp_addr = main_addr + '/tupian/' + xtp + ".html"
        print('xtp_addr = ' + xtp_addr)
        da_tu_pian = get_addr('/uploads/allimg/(.*?).jpg', get_html(xtp_addr))
        dtp_addr = main_addr + '/uploads/allimg/' + da_tu_pian[0] + '.jpg'
        print('dtp_addr = ' + dtp_addr)
        save_addr = './4kdongman/' + da_tu_pian[0].split("/")[1] + '.jpg'
        print("save_addr = " + save_addr)
        download_img(dtp_addr, save_addr)

def get_addr(pat, html_data):
    result = re.compile(pat).findall(html_data)
    return result

def get_html(url):
    page_data = urllib.request.urlopen(url)
    html_a = page_data.read()
    return html_a.decode('cp936')

def download_img(img_addr, save_addr):
    urllib.request.urlretrieve(img_addr, save_addr)

if __name__ == "__main__":
    main()
