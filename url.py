#!/usr/bin/env python
# coding=utf-8
import urllib,re,requests,sys,datetime
oknum=nonum=wrong=find1=find2=unknow=0
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
            if res == '':
                wrong=wrong+1
            #elif not rest:print rest
            else:
                if res == None:
                    wrong=wrong+1
                elif str(proto) == 'http':
                    fulldomain= str(proto)+'://'+ res
                    fullpath=str(proto)+'://'+ res + rest
                    domain_list.append(fulldomain)
                    path_list.append(fullpath)
                    find1=find1+1
                elif str(proto) == 'https':
                    fulldomain= str(proto)+'://' + res
                    fullpath=str(proto)+'://'+ res + rest
                    domain_list.append(fulldomain)
                    path_list.append(fullpath)
                    find2=find2+1
                else:unknow=unknow+1
indomain.close()
output_domain = open("ok/fulldomain.txt", "w+")
domain_list_t=set(domain_list)
for m in domain_list_t:
    output_domain.write(str(m+'\n'))
output_domain.close()

path_list_t=set(path_list)
output_path = open("ok/fullpath.txt", "w+")
for n in path_list_t:
    output_path.write(str(n+'\n'))
output_path.close()
print 'success '+str(oknum)+' domain'
print 'find http '+str(find1)
print 'find https '+str(find2)
print 'find urls '+str(find1+find2)
print 'lose '+str(nonum)+' domains'
print 'bad url '+str(wrong)+' unknow wrong '+str(unknow)
end = datetime.datetime.now()
print 'use time '+str(end-start)
