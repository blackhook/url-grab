#!/usr/bin/env python
# coding=utf-8
import urllib,re,requests,sys,os,datetime
oknum=0
nonum=0
reload(sys)
sys.setdefaultencoding( "utf-8" )
out=open("temp/temp","a")
indomain=open("in.txt")
start = datetime.datetime.now()
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
for line in indomain:
    line=line.strip('\n')
    try:
        r = requests.get(line,verify=True,timeout=2,headers=headers)
        oknum=oknum+1
        print str(oknum)+'ok!!!'
    except requests.RequestException as e:
        print line+'  cannot read';
        nonum=nonum+1
    else:
        data = r.text
        link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
        for url in link_list:
            proto, rest = urllib.splittype(url)
            res, rest = urllib.splithost(rest)
            #outtxt = str(res).encode('raw-unicode-escape');
            outtxt = str(res)
            #print "" if not res else res
            out.write(outtxt+'\n')
out.close()
input = open("temp/temp", "r").read()
output = open("ok/ok.txt", "w+")
output.write('\nhttp://'.join(set(input.split('\n'))))
output.close()
filename = 'temp/temp'
os.remove(filename)
print 'success '+str(oknum)+' domains'
print 'lose '+str(nonum)+' domains'
end = datetime.datetime.now()
print 'use time '+str(end-start)