import requests


def download(source: str):
    res = requests.get(source)
    return res.content


def downloadToFile(source: str, dest: int):
    content = download(source)
    file = open(dest, 'wb')
    file.write(content)
    file.close()
    return file
