#-*-coding:utf-8-*-

import  requests

headers = {
    'Cookie':'_zap=25f0933e-e485-49ba-8c61-0bb0d971669a; d_c0="ACAibU7ACA-PTsXIL6FZTmrM-rt2Sp8GhWY=|1551065320"; z_c0="2|1:0|10:1553564907|4:z_c0|92:Mi4xcEJ6d0RnQUFBQUFBSUNKdFRzQUlEeVlBQUFCZ0FsVk42dEtHWFFDWV9jaWlEMVdtWVBuLUpSX0RDY2l6SE9HbzFn|1a76354d264ab7ce3ecc2d1d92edec49ca562e65d29cd9ce51893336886a26af"; tst=r; __utma=51854390.583315880.1553565631.1553565631.1553565631.1; __utmz=51854390.1553565631.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20190326=1^3=entry_date=20190326=1; q_c1=43ae09260e44481999b570afc3885c08|1556420936000|1553565122000; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; _xsrf=3e07066d-9a8f-4f37-9388-4770e674e96c',

    'Host':'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',

}

r  =requests.get("https://www.zhihu.com" , headers = headers)
print(r.text)