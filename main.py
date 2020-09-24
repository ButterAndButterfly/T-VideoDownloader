from core.kuaishou import Kuaishou
import json
import time

if __name__ == '__main__':
    # 读取配置
    with open(r'config.json', "r", encoding='utf-8') as file:
        content = file.read()
        print(content)
        config = json.loads(content)
        
    for task in config['tasks']:
        # 获取时间
        if 'time_min' in task:
            time_min = task['time_min']
        elif 'time_min' in config:
            time_min = config['time_min']
        else:
            time_min = None
            
        if 'time_max' in task:
            time_max = task['time_max']
        elif 'time_max' in config:
            time_max = config['time_max']
        else:
            time_max = None
        # 获取任务id
        if 'user_id' in task:
            user_id = task['user_id']
        else:
            user_id = task
        
        print(time_max)
        downloader = Kuaishou(
            cookie=config['cookie'],
            user_id=user_id,
            time_min=time_min,
            time_max=time_max,
        )
        videos = downloader.getVideos()
        for index, video in enumerate(videos):
            print(video['video_id'])
            
        print('正在下载 id为 %s的视频，共有%d 个' % (user_id , len(videos)))
        for index, video in enumerate(videos):
            # 下载文件夹
            folder = config['saveFolder']\
                .replace('{user_name}', video['user_name'])\
                .replace('{user_id}', video['user_id'])\
                .replace('{caption}', video['caption'])
            # 下载文件名
            fileName = None
            if 'fileName' in config:
                fileName = config['fileName']\
                    .replace('{user_name}', video['user_name'])\
                    .replace('{user_id}', video['user_id'])\
                    .replace('{video_id}', video['video_id'])\
                    .replace('{caption}', video['caption'])

            print('下载进度： %d/%d' % (index + 1, len(videos)))
            dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(video['timestamp']/1000.0))
            print('发布日期： %s' % dtime)
            url = downloader.getUrl(video['user_id'], video['video_id'])
            print('下载链接： %s' % url)
            downloader.download(url, folder=folder, fileName=fileName)
            print('%s 下载完毕' % video['caption'])
