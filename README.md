# Tiny-Video Downloader
专注于**短**视频**批量**下载，暂只支持快手  


## 功能  
批量下载指定用户的所有/特定视频(可以限定日期，老旧视频不再下载)

## 用户测评(本人??)  
比自己手动一个一个下要快那么一点，然后频率太快蛮容易报异常的，查询之间最好sleep几秒  

## 如何配置  
+ 将`app.json`配置好即可，以下为示例：  
```json
{
    "cookie": "clientid=x; did=xx; client_key=xxx; ...",
    "saveFolder": "D:\\Downloads\\{user_name}",
    "fileName": "{default}",
    "tasks": 
    [
        {
            "user_id": "lolxingchen",
            "time_min": "2020-05-29",
            "time_max": "2020-05-31"
        },
        {
            "user_id": "lolxingchen",
            "time_min": "2020-05-29"
        },
        {
            "user_id": "lolxingchen",
            "time_max": "2020-05-31"
        },
        {
            "user_id": "lolxingchen"
        },
        "lolxingchen"
    ]
}
```

+ 需要cookie配合，请注意cookie容易过期(比如查询次数多了以后)，此时需要打开浏览器页面刷一下页面使之重新生效  
+ `saveFolder`为保存路径，支持变量`{user_name}`、`{user_id}`、`{caption}`  
+ `fileName`为保存文件名称，支持变量`{user_name}`、`{user_id}`、`{caption}`以及`{default}`  
    + 其中，{default}为下载链接尾部有效的那一部分  
+ `tasks`为任务列表，除`user_id`外其它可缺省，支持示例中的各种写法  
+ `user_id`为用户id，一般来说，就是url后面那一部分  
    + 比如`https://live.kuaishou.com/profile/lolxingchen`，用户id为`lolxingchen`  
+ `time_min`为边界日期，只会查询在这之后的视频。默认为None，此时不作条件限制。  
+ `time_max`为边界日期，只会查询在这之前的视频。默认为None，此时不作条件限制。  
+ 如果下载的文件已经存在，那么虽然会进行下载链接查询，但不会重复再下载  

## 如何运行  
```
pip install -r requirements.txt

python main.py 
```

## License  

The Star And Thank Author License (SATA)