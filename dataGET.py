import time
import requests

def getFurParty():
    """
    调用后获得全部兽聚信息\n
    返回 聚会的 JSON 文件
    """
    # API的URL（替换为实际的API URL）
    # url = "https://api.furryfusion.net/service/countdown?mode=1" # 倒计时URL
    url = 'https://api.furryfusion.net/service/activity?mode=1' # 活动档期URL
    # 动态生成时间戳
    timestamp = int(time.time())

    # 请求头
    headers = {
        'User-Agent': 'MyApp/1.0',
        'X-Timestamp': str(timestamp)  # 动态添加时间戳
    }

    # 发送GET请求获取数据
    response = requests.get(url,headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 如果成功，获取响应的JSON数据
        data = response.json()  # 返回一个字典格式的数据
        return data
    else:
        # 如果请求失败，返回错误信息
        data = {
            "code":"Error",
            "source":f"请求失败，状态码：{response.status_code}"
        }
        return data