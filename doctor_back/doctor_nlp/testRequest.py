import requests


def call_search_database(query):
    # 这里假设你在本地运行Django服务，端口号是8000
    url = "http://127.0.0.1:8000/restapi/search/"

    # 使用POST请求发送数据
    response = requests.post(url, json={"query": query})

    if response.status_code == 200:
        print("Search Results:")
        for result in response.json().get('results', []):
            print(result)
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    query = input("Test: 发送POST请求至/restapi/search/\n请输入查询字符串: ")
    call_search_database(query)
