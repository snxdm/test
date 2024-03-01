import requests

def upload_file_to_github(file_path, repository, branch, token):
    # 读取文件内容
    with open(file_path, 'rb') as file:
        content = file.read()
    # 构建GitHub API URL
    url = f'https://api.github.com/repos/{repository}/contents/{file_path}'
    # 构建请求头
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    # 构建请求体
    data = {
        'message': 'Upload file via bot',
        'content': content,
        'branch': branch
    }
    # 发送上传文件请求
    response = requests.put(url, headers=headers, files={'file': content})
    return response.json()