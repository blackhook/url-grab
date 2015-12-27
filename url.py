#!/usr/bin/env python
# coding=utf-8
import urllib,re,requests,sys,datetime
logo="""
 _   _ ____  _        ____ ____      _    ____
| | | |  _ \| |      / ___|  _ \    / \  | __ )
| | | | |_) | |     | |  _| |_) |  / _ \ |  _ |
| |_| |  _ <| |___  | |_| |  _ <  / ___ \| |_) |
 \___/|_| \_\_____|  \____|_| \_\/_/   \_\____/
"""
print logo
oknum=nonum=wrong=find1=find2=unknow=0
reload(sys)
sys.setdefaultencoding( "utf-8" )
indomain=open("in.txt")
incount=len(open('in.txt','rU').readlines())
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
        print '('+str(oknum)+"/"+str(incount)+')'+' '+line+' ok'
    except requests.RequestException as e:
        oknum=oknum+1
        nonum=nonum+1
        print '('+str(oknum)+"/"+str(incount)+')'+' '+line+' cannot read';
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
print '--'*40
print 'success '+str(oknum)+' domain'
print 'lose '+str(nonum)+' domains'
print 'find http '+str(find1)
print 'find https '+str(find2)
print 'find urls '+str(find1+find2)
print 'find distinct domain '+str(len(open('ok/fulldomain.txt','rU').readlines()))+' distinct path '+str(len(open('ok/fullpath.txt','rU').readlines()))
print 'bad url '+str(wrong)+' unknow wrong '+str(unknow)
end = datetime.datetime.now()
print 'use time '+str(end-start)
print '--'*40