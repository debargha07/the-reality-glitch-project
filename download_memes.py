import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

memes = [
    ("meme-01.jpg", "https://i.imgflip.com/9vj3ue.jpg"),
    ("meme-03.jpg", "https://i.imgflip.com/9vj3wd.jpg"),
    ("meme-04.jpg", "https://i.imgflip.com/9vj3xc.jpg"),
    ("meme-05.jpg", "https://i.imgflip.com/9vj3yb.jpg"),
    ("meme-06.jpg", "https://i.imgflip.com/9vj3za.jpg"),
    ("meme-07.jpg", "https://i.imgflip.com/9vj40z.jpg"),
    ("meme-08.jpg", "https://i.imgflip.com/9vj41y.jpg"),
    ("meme-09.jpg", "https://i.imgflip.com/9vj42x.jpg"),
    ("meme-10.jpg", "https://i.imgflip.com/1g8my4.jpg"),
    ("meme-11.jpg", "https://i.imgflip.com/39t1vc.jpg"),
]

for filename, url in memes:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(f"assets/memes/{filename}", 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
