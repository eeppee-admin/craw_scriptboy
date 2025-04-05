import requests
import os
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 加载环境变量
load_dotenv()

# 配置重试策略
session = requests.Session()
retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

# 请求头配置
headers = {
    "X-Rapidapi-Host": "porn-image1.p.rapidapi.com",
    "X-Rapidapi-Key": os.getenv("RAPIDAPI_KEY"),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_image():
    try:
        response = session.get(
            "https://porn-image1.p.rapidapi.com/",
            headers=headers,
            params={"type": "pussy"},
            timeout=10
        )
        
        response.raise_for_status()
        json_data = response.json()
        
        if json_data.get("success"):
            return json_data["url"]
        return None

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    image_url = fetch_image()
    if image_url:
        print(f"成功获取资源地址：{image_url}")
    else:
        print("未能获取有效数据")