import re
import requests
import json

try:
    # 发送HTTP请求获取网页内容
    response = requests.get("https://imcys.com")
    response.encoding = 'utf-8'  # 显式指定编码
    html_content = response.text
    
    # 正则表达式匹配（优化非贪婪模式）
    title_pattern = re.compile(r'title="(.*?)" class=')
    image_pattern = re.compile(r'alt="(.*?)" title')
    url_pattern = re.compile(r'<a href="(.*?)" rel=')
    
    # 提取数据
    title_list = title_pattern.findall(html_content)
    image_list = image_pattern.findall(html_content)
    url_list = url_pattern.findall(html_content)
    
    # 组合JSON数据（处理长度不一致问题）
    min_length = min(len(title_list), len(image_list), len(url_list))
    json_data = [
        {
            "title": title_list[i],
            "image": image_list[i],
            "url": url_list[i]
        } for i in range(min_length)
    ]
    
    # 输出格式化JSON
    print(json.dumps(json_data, indent=2, ensure_ascii=False))
    
except requests.exceptions.RequestException as e:
    print(f"网络请求失败: {e}")
except Exception as e:
    print(f"程序异常: {e}")