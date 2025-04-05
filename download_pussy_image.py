import requests
from concurrent.futures import ThreadPoolExecutor
import os

# RapidAPI 配置（需替换为实际密钥）
API_KEY = "e8a0cab8femsh32ae72fd76831c8p1a1993jsnd685db6b7c3a"
API_HOST = "porn-image1.p.rapidapi.com"
API_ENDPOINT = "https://porn-image1.p.rapidapi.com/"

def fetch_resource_urls(resource_type="pussy", count=10):
    """批量获取资源地址[1,4](@ref)"""
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    
    resource_urls = []
    for _ in range(count):
        try:
            response = requests.get(
                API_ENDPOINT,
                params={"type": resource_type},
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
            if data.get("success"):
                resource_urls.append(data["url"])
        except Exception as e:
            print(f"获取资源失败: {str(e)}")
    
    return resource_urls

def download_file(url, save_dir="downloads"):
    """多线程下载文件[6,7](@ref)"""
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        filename = os.path.join(save_dir, url.split('/')[-1])
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"成功下载: {filename}")
        return True
    except Exception as e:
        print(f"下载失败: {url} - {str(e)}")
        return False

if __name__ == "__main__":
    # 获取10个资源地址
    urls = fetch_resource_urls(count=10)
    print(f"获取到 {len(urls)} 个资源地址")
    
    # 多线程下载（最大5线程）
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_file, url) for url in urls]
        results = [future.result() for future in futures]
    
    print(f"下载完成，成功率: {sum(results)}/{len(urls)}")