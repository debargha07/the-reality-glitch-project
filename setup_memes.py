import os
from PIL import Image, ImageDraw, ImageFont

MEMES = [
  ("meme-01.jpg", "THIS IS FINE"),
  ("meme-02.jpg", "SURPRISED PIKACHU"),
  ("meme-03.jpg", "DISTRACTED BF"),
  ("meme-04.jpg", "GALAXY BRAIN"),
  ("meme-05.jpg", "CRYING CAT"),
  ("meme-06.jpg", "STONKS"),
  ("meme-07.jpg", "WE DON'T DO THAT"),
  ("meme-08.jpg", "WAIT ILLEGAL"),
  ("meme-09.jpg", "DRAKE POINTING"),
  ("meme-10.jpg", "WOMAN VS CAT"),
  ("meme-11.jpg", "UNO REVERSE"),
]

os.makedirs("assets/memes", exist_ok=True)

colors = [
  "#1a1a2e","#16213e","#0f3460","#1b1b2f",
  "#2d132c","#1a1a1a","#0d0d0d","#111122",
  "#1e1e2e","#0a0a1a","#1c1c2e"
]

for i, (filename, label) in enumerate(MEMES):
    img = Image.new("RGB", (400, 300), color=colors[i % len(colors)])
    draw = ImageDraw.Draw(img)

    # border
    draw.rectangle([4,4,395,295], outline="#00ffe7", width=3)

    # label
    draw.text((200, 130), label, fill="#ffffff", anchor="mm")
    draw.text((200, 165), f"[REPLACE WITH REAL MEME]", fill="#ff2244", anchor="mm")
    draw.text((200, 195), filename, fill="#888888", anchor="mm")

    img.save(f"assets/memes/{filename}", quality=90)
    print(f"Created {filename}")

print("\nDone. Replace placeholders with real meme images.")
print("Keep filenames exactly: meme-01.jpg through meme-11.jpg")
