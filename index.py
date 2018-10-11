from lib.download import download

source = 'https://farm5.staticflickr.com/4259/35163667010_8bfcaef274_k_d.jpg'
dest = 'image.jpg'

file = download(source, dest)

print(file)
