# # 下载5张pussy类型图片
# python downloader.py --type pussy --count 5

# # # 使用默认参数下载1张
# python downloader.py
import argparse
import requests
import os
import time
import random

def download_images():
    parser = argparse.ArgumentParser(description='图片下载器')
    parser.add_argument('--type', default='pussy', help='图片类型')
    parser.add_argument('--count', type=int, default=1, help='下载数量')
    args = parser.parse_args()

    # 创建下载目录
    download_dir = 'downloads'
    os.makedirs(download_dir, exist_ok=True)

    # API配置
    headers = {
        "X-Rapidapi-Key": "e8a0cab8femsh32ae72fd76831c8p1a1993jsnd685db6b7c3a",
        "X-Rapidapi-Host": "girls-nude-image.p.rapidapi.com"
    }

    success_count = 0
    for i in range(args.count):
        try:
            # 获取图片URL
            response = requests.get(
                "https://girls-nude-image.p.rapidapi.com/",
                headers=headers,
                params={"type": args.type}
            )
            data = response.json()

            if data.get("success"):
                # 下载图片
                img_url = data["url"]
                img_data = requests.get(img_url, stream=True).content
                
                # 生成唯一文件名
                filename = f"{int(time.time())}_{random.randint(1000,9999)}.jpg"
                save_path = os.path.join(download_dir, filename)
                
                # 保存文件
                with open(save_path, 'wb') as f:
                    f.write(img_data)
                print(f"已下载: {save_path}")
                success_count += 1

        except Exception as e:
            print(f"下载失败: {str(e)}")

    print(f"\n下载完成，成功 {success_count}/{args.count} 个文件")

if __name__ == "__main__":
    download_images()