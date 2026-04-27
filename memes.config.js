// ─────────────────────────────────────────
// MEME REGISTRY — memes.config.js
// Add new memes here. HTML auto-reads this.
// ─────────────────────────────────────────

const MEME_REGISTRY = [
  {
    id: "meme-01",
    src: "assets/memes/meme-01.jpg",
    caption: "THIS IS FINE.",
    alt: "dog sitting in burning room",
    weight: 1           // higher = appears more often
  },
  {
    id: "meme-02",
    src: "assets/memes/meme-02.jpg",
    caption: "HAKLA",
    alt: "funny hakla meme",
    weight: 1
  },
  {
    id: "meme-03",
    src: "assets/memes/meme-03.jpg",
    caption: "DISTRACTED AGAIN.",
    alt: "distracted boyfriend",
    weight: 1
  },
  {
    id: "meme-04",
    src: "assets/memes/meme-04.jpg",
    caption: "BIG BRAIN MOMENT.",
    alt: "galaxy brain expanding",
    weight: 2
  },
  {
    id: "meme-05",
    src: "assets/memes/meme-05.jpg",
    caption: "MOOD: ALWAYS.",
    alt: "crying cat at dinner table",
    weight: 1
  },
  {
    id: "meme-06",
    src: "assets/memes/meme-06.jpg",
    caption: "STONKS ONLY GO UP.",
    alt: "stonks meme guy",
    weight: 1
  },
  {
    id: "meme-07",
    src: "assets/memes/meme-07.jpg",
    caption: "WE DON'T DO THAT HERE.",
    alt: "black panther we don't do that here",
    weight: 1
  },
  {
    id: "meme-08",
    src: "assets/memes/meme-08.jpg",
    caption: "WAIT. THAT'S ILLEGAL.",
    alt: "wait that's illegal meme",
    weight: 1
  },
  {
    id: "meme-09",
    src: "assets/memes/meme-09.jpg",
    caption: "REALITY CHOSE THIS.",
    alt: "drake pointing approved meme",
    weight: 2
  },
  {
    id: "meme-10",
    src: "assets/memes/meme-10.jpg",
    caption: "EXPLAIN. NOW.",
    alt: "woman yelling at cat",
    weight: 1
  },
  {
    id: "meme-11",
    src: "assets/memes/meme-11.jpg",
    caption: "UNO REVERSE: ACTIVATED.",
    alt: "uno reverse card meme",
    weight: 1
  }
];

// ─────────────────────────────────────────
// WEIGHTED RANDOM PICKER
// Respects the weight field so some memes
// appear more frequently than others
// ─────────────────────────────────────────

function pickMeme() {
  const pool = [];
  MEME_REGISTRY.forEach(m => {
    for (let i = 0; i < m.weight; i++) pool.push(m);
  });
  return pool[Math.floor(Math.random() * pool.length)];
}

// ─────────────────────────────────────────
// PICK N UNIQUE MEMES (no repeats in same wave)
// ─────────────────────────────────────────

function pickUniqueMemes(count) {
  const shuffled = [...MEME_REGISTRY].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(count, MEME_REGISTRY.length));
}
