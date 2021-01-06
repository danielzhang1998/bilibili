import re, ssl
import requests

def open_url(url):
# encoding: utf-8
 
    headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html',
    'Cookie': "_uuid=1DBA4F96-2E63-8488-DC25-B8623EFF40E773841infoc; buvid3=FE0D3174-E871-4A3E-877C-A4ED86E20523155831infoc; LIVE_BUVID=AUTO8515670521735348; sid=l765gx48; DedeUserID=33717177; DedeUserID__ckMd5=be4de02fd64f0e56; SESSDATA=cf65a5e0%2C1569644183%2Cc4de7381; bili_jct=1e8cdbb5755b4ecd0346761a121650f5; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(umY))|ukl~0J'ulY~uJm)kJ; UM_distinctid=16ce0e51cf0abc-02da63c2df0b4b-5373e62-1fa400-16ce0e51cf18d8; stardustpgcv=0606; im_notify_type_33717177=0; finger=b3372c5f; CURRENT_QUALITY=112; bp_t_offset_33717177=300203628285382610"
    
    }
    f = open('testing_new.txt','w')
    ssl._create_default_https_context = ssl._create_unverified_context
    html = requests.get(url,headers=headers).text # 获取url内容
    f.write(html) # 写入 url内容到文件，决定如何写下面的正则表达式
    f.close()
    return html

def get_durations(url):
    html = open_url(url)
    m = r'"cid":.+?,'
    match = str(re.findall(m, html)[0])
    match = match.split(':')[-1]
    match = match.split(',')[0] # 获得第一个视频的 cid 用来辅助获取完整的播放列表
    p = r'\[{"cid":' + match + '.+?]'
    pic = re.findall(p, html)  # 获取完整的播放列表
    final_result = []
    q = r'"duration":.+?,'
    pic = str(pic)
    duration = re.findall(q, pic)   # 获取每一个视频的播放时长的列表（此处包含了 class 名称，需要进一步进行处理）
    duration = str(duration)
    y = r':.+?,'
    time_get = re.findall(y, duration)  # 获得每一个视频的播放时长列表（进一步进行处理）

    for each in range(len(time_get)):   # 清除所有不必要的内容
        time_get[each] = time_get[each].split(':')[-1]
        time_get[each] = time_get[each].split(',')[0]
        temp = time_get[each]
        final_result.append([int(temp) // 60, int(temp) % 60])  # 将时间转换成 分钟:秒
    return final_result

if __name__ == '__main__':
    url = input('enter\n')
    #open_url(url)
    get_durations(url)
