# Tiny-Video Downloader
רע��**��**��Ƶ**����**���أ���ֻ֧�ֿ���  


## ����  
��������ָ���û�������/�ض���Ƶ(�����޶����ڣ��Ͼ���Ƶ��������)

## �û�����(����??)  
���Լ��ֶ�һ��һ����Ҫ����ôһ�㣬Ȼ��Ƶ��̫�������ױ��쳣�ģ���ѯ֮�����sleep����  

## �������  
+ ��`app.json`���úü��ɣ�����Ϊʾ����  
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

+ ��Ҫcookie��ϣ���ע��cookie���׹���(�����ѯ���������Ժ�)����ʱ��Ҫ�������ҳ��ˢһ��ҳ��ʹ֮������Ч  
+ `saveFolder`Ϊ����·����֧�ֱ���`{user_name}`��`{user_id}`��`{caption}`  
+ `fileName`Ϊ�����ļ����ƣ�֧�ֱ���`{user_name}`��`{user_id}`��`{caption}`�Լ�`{default}`  
    + ���У�{default}Ϊ��������β����Ч����һ����  
+ `tasks`Ϊ�����б���`user_id`��������ȱʡ��֧��ʾ���еĸ���д��  
+ `user_id`Ϊ�û�id��һ����˵������url������һ����  
    + ����`https://live.kuaishou.com/profile/lolxingchen`���û�idΪ`lolxingchen`  
+ `time_min`Ϊ�߽����ڣ�ֻ���ѯ����֮�����Ƶ��Ĭ��ΪNone����ʱ�����������ơ�  
+ `time_max`Ϊ�߽����ڣ�ֻ���ѯ����֮ǰ����Ƶ��Ĭ��ΪNone����ʱ�����������ơ�  
+ ������ص��ļ��Ѿ����ڣ���ô��Ȼ������������Ӳ�ѯ���������ظ�������  

## �������  
```
pip install -r requirements.txt

python main.py 
```

## License  

The Star And Thank Author License (SATA)