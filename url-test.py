#!/usr/bin/env python
# coding=utf-8
import urllib,re,requests,sys,datetime
oknum=nonum=0
reload(sys)
sys.setdefaultencoding( "utf-8" )
indomain=open("in.txt")
path_list = []
domain_list = []
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
                    fulldomain= str(proto)+'://'+res
                    fullpath=str(proto)+'://'+res+rest
                    domain_list.append(fulldomain)
                    path_list.append(fullpath)
                elif str(proto) == 'https':
                    fulldomain= str(proto)+'://'+res
                    fullpath=str(proto)+'://'+res+rest
                    domain_list.append(fulldomain)
                    path_list.append(fullpath)
                else:
                    break

output_domain = open("ok/fulldomain.txt", "w+")
output_path = open("ok/fullpath.txt", "w+")
domain_list_t=set(domain_list)
for i in domain_list_t:
    output_domain.write(str(i+'\n'))
path_list_t=set(domain_list)
for i in path_list_t:
    output_path.write(str(i+'\n'))
indomain.close()
output_domain.close()
output_path.close()
print 'success '+str(oknum)+' domains'
print 'lose '+str(nonum)+' domains'
end = datetime.datetime.now()
print 'use time '+str(end-start)