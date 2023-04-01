import requests
import pandas as pd
from bs4 import BeautifulSoup

# 设置请求头部信息，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# 定义一个函数，用于获取帆船的year属性和价格数据
def get_yacht_data(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # 获取帆船的year属性和价格数据
    year = soup.find('span', {'class': 'year'}).text.strip()
    price = soup.find('span', {'class': 'price'}).text.strip()

    # 返回帆船的year属性和价格数据
    return {'year': year, 'price': price}

# 定义一个主函数，用于爬取所有帆船的year属性和价格数据，并将它们存储到CSV文件中
def main():
    # 设置YachtWorld网站上的搜索条件
    search_params = {
        'class': 'sail',
        'price': 'USD100000-500000',
        'length': '40-50ft'
    }
    base_url = 'https://www.yachtworld.com'

    # 发出HTTP请求，获取搜索结果页面
    res = requests.get(f'{base_url}/boats-for-sale/', params=search_params, headers=headers)
    # print(res.content)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.contents)
    for a in soup.select('.tile-info h2 a'):
        print(a)

    # 获取搜索结果页面中所有帆船的详情页链接
    yacht_links = [f'{base_url}{a["href"]}' for a in soup.select('.tile-info h2 a')]

    # 爬取所有帆船的year属性和价格数据，并将它们存储到CSV文件中
    yacht_data_list = []
    for link in yacht_links:
        yacht_data = get_yacht_data(link)
        yacht_data_list.append(yacht_data)
    df = pd.DataFrame(yacht_data_list)
    df.to_csv('yacht_data.csv', index=False)

if __name__ == '__main__':
    main()
