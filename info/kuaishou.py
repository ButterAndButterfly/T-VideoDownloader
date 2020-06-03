# coding=utf-8
import requests
import csv

class Kuaishou:

    def __init__(self, cookie):
        self.cookie = cookie
        self.follows = []
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Content-Type': 'application/json',
            'Origin': 'https://live.kuaishou.com',
            'Host': 'live.kuaishou.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Referer': 'https://live.kuaishou.com/cate/my-follow/all',
            'Cookie': self.cookie
        }
    
        
    def getFollows(self):
        url = "https://live.kuaishou.com/m_graphql"
        pcursor = ""
        while pcursor != 'no_more':
            param = '{"operationName":"FollowQuery","variables":{"count":100,"pcursor":"%s"},"query":\
            "query FollowQuery($pcursor: String, $count: Int) {\\n  allFollows(pcursor: $pcursor, count: $count)\
             {\\n    list {\\n      id\\n      name\\n      living\\n      avatar\\n      sex\\n      description\\n\
             counts {\\n        fan\\n        follow\\n        photo\\n        __typename\\n      }\\n\
             __typename\\n    }\\n    pcursor\\n    __typename\\n  }\\n}\\n"}' % (pcursor)
            data = requests.post(url, timeout=10, headers=self.headers, data=param)
            data = data.json()['data']['allFollows']
            pcursor = data['pcursor']
            for user in data['list']:
                user = {
                    'id': user['id'],
                    'name': user['name'],
                    'sex': user['sex'],
                    'avatar': user['avatar'],
                    'description': user['description'],
                }
                self.follows.append(user)
                
        return self.follows

    
if __name__ == '__main__':
    api = Kuaishou(
#         cookie='',
    )
    follows = api.getFollows()
    print('共有%d 个关注' % len(follows))
    with open('data.csv','w',newline='', encoding='utf-8-sig') as fp:
        writer = csv.writer(fp)
        for index, user in enumerate(follows):
            print('%s\t%s\thttps://live.kuaishou.com/profile/%s'%(user['id'], user['name'], user['id']))
            writer.writerow([user['id'],user['name'],'https://live.kuaishou.com/profile/%s'%user['id']])
