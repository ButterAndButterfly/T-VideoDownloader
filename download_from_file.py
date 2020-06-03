from core.kuaishou import Kuaishou
import json

if __name__ == '__main__':
    '''
    main.py报错的一点补救措施，用于下载user_id用户的特定视频
        user_id(必需)，
        user_name(如果自定义文件名中没有那就不需要)，
        file.txt(一行一个video_id，main.py有打印，按需删减)
    '''
    user_id = ''
    user_name = ''
    # 读取配置 每行一个video id
    with open(r'config.json', "r") as file:
        content = file.read()
        config = json.loads(content)
        
    downloader = Kuaishou(
        cookie=config['cookie'],
        user_id=user_id,
    )
    with open(r'file.txt', "r") as file:
        
        line = file.readline().strip('\r\n')
        while line:
            video = {
                'user_name': user_name,
                'user_id': user_id,
                'video_id': line,
            }
            # 下载文件夹
            folder = config['saveFolder']\
                .replace('{user_name}', video['user_name'])\
                .replace('{user_id}', video['user_id'])\
            # 下载文件名
            fileName = None
            if 'fileName' in config:
                fileName = config['fileName']\
                    .replace('{user_name}', video['user_name'])\
                    .replace('{user_id}', video['user_id'])\
                    .replace('{video_id}', video['video_id'])\
    
            url = downloader.getUrl(video['user_id'], video['video_id'])
            print('下载链接： %s' % url)
            downloader.download(url, folder=folder, fileName=fileName)
            line = file.readline().strip('\r\n')
