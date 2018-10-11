from requests import get


def download(source: str, dest: int):
    res = get(source)
    file = open(dest, 'wb')
    file.write(res.content)
    file.close()
    return file
