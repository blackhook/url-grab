#!/usr/bin/env python
# coding=utf-8
import urllib,re,requests,sys,os,datetime
oknum=0
nonum=0
reload(sys)
sys.setdefaultencoding( "utf-8" )
domaintemp=open("domain_temp","a")
pathtemp=open("path_temp","a")
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
            if  res == '' :
                break
            elif not rest:break
            elif not proto:break
            else:
                if str(proto) == 'http':
                    fullurl= str(proto)+'://'+res
                    fullpath=str(proto)+'://'+res+rest
                    pathtemp.write(fullpath+'\n')
                    domaintemp.write(fullurl+'\n')
                elif str(proto) == 'https':
                    fullurl= str(proto)+'://'+res
                    fullpath=str(proto)+'://'+res+rest
                    pathtemp.write(fullpath+'\n')
                    domaintemp.write(fullurl+'\n')
                else:
                    break
domaintemp.close()
pathtemp.close()
indomain.close()

domain_temp_input = open("domain_temp", "r").read()
output_domain = open("ok/fulldomain.txt", "w+")
output_domain.write('\n'.join(set(domain_temp_input.split('\n'))))
output_domain.close()
temp1 = 'domain_temp'
os.remove(temp1)

path_temp_input = open("path_temp", "r").read()
out_path = open("ok/fullpath.txt", "w+")
out_path.write('\n'.join(set(path_temp_input.split('\n'))))
out_path.close()
temp2 = 'path_temp'
os.remove(temp2)

print 'success '+str(oknum)+' domains'
print 'lose '+str(nonum)+' domains'
end = datetime.datetime.now()
print 'use time '+str(end-start)