import requests
import json
import re
url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_25906124?csrf_token=4685d88c2e3c1a1bbba082f6139ec567'
param={'params':'90gNJHNnnb+qbMwml4A39ZhcHVWL25aYIefRp0a1PdNvydwNiqlCr9akwOuhQXJazItBTYd4/SAVUR2IEe+Hn6HXipUTy4FCL7j3Ufib\
17YXOmpaYkgXUe5ujgrihClru1fyfeFjmLNSuE9aeOK8OENeaiBNaExVg4kwFYYiy0h3FQn+5D9lgOAtrxNhnz0ioDoR6ek/wZ+hn4PDlZPT7OlRN79Hs45I\
95vnYVyTBRw=','encSecKey':'9372a2b5ad22e2eeaa8a5a175935f78fd3f88e5b323b4786d29dd1faddc8d17c5ec0555d2b60a23fe49c5c56b92b5\
3e16c9a259a1850c04b4519fbb27373008bf73c06e4b9fdb089f684c70f9b9b67b2218a174066df56078ef8916d4118afd84ea2372f91b1336e0ac18\
790b1cfac6296c8c9d3e1525b783d044e6ae5a66405'}
r=requests.post(url,param)
date=r.text
jsob=json.loads(date)
hotComments=jsob['hotComments']

with open('comments.txt','w') as f:
    for i in range(len(hotComments)):
        u_nickname=hotComments[i]['user']['nickname']
        likeCount=hotComments[i]['likedCount']
        content=hotComments[i]['content']

        f.write(u'评论'+str(i)+'   'u'用户名: '+str(u_nickname)+'  '+u'赞: '+str(likeCount))
        f.write('\n')
        l = len(content)  # 字符串长度
        n = 1  # 计数，每40个字符换行，重新计数
        for i in range(l):
            f.write(content[i])
            if n == 40:
                f.write('\n')
                n = 0

            n += 1
        f.write('\n'*2)







