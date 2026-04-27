# The Reality Glitch Project 🌀


## The Idea 💡
Hey! I'm Debargha, and this is my **Reality Glitch** project. I wanted to build something weird, interactive, and a little bit frustrating on purpose. The idea was to create a web page that feels like a compromised, glitchy system that actively trolls the user.
Instead of building a normal landing page, I built a "system error" simulator. It features a button you can't click because it dodges your mouse, fake error notifications that spam your screen if you try to report a bug, and a "Meme Avalanche" that drops random memes all over the page if you give it permission.

## Tech Stack 
I kept the core stack pretty vanilla because I wanted to see how far I could push standard web tech without a heavy framework:
*   **HTML/CSS:** For the layout and all the crazy visual effects (like the CRT scanlines, RGB tearing, and the SVG noise grain).
*   **Vanilla JavaScript:** To handle all the logic, event listeners, and tracking the mouse coordinates.
*   **GSAP (GreenSock):** This was the heavy lifter for all the smooth animations. I used it for the dodging button, the meme drops, and the notification bounces.
*   **Baffle.js:** Used this tiny library for that cool scrambling hacker-text effect on the subtitle.
*   **Python:** I wrote some helper scripts (`download_memes.py`, `setup_memes.py`, `create_audio_config.py`) to automate downloading meme images from Imgflip and converting assets into JS config files so everything runs smoothly locally.
*   **Vercel:** For deployment!

## Architecture Plan 
Since I wanted this to be lightweight, my plan was a single-page architecture:
1.  **`reality-glitch.html`:** The main hub. I put all the CSS and JS right in here to make it a self-contained experience. 
2.  **Asset Pipeline:** Instead of manually handling images and audio, I built a mini pipeline with Python. The Python scripts download the assets and generate `memes.config.js` and `audio.config.js`. The HTML file just links to these configs.
3.  **Layering System:** I had to carefully plan the z-indexes. Background effects at the very back, main UI in the middle, and the dodging buttons, notifications, and meme cards overlapping everything at the very front.

## Challenges I Faced 
This project was super fun but definitely had some headaches:
*   **The Dodging Button Math:** Getting the button to teleport away from the mouse *smoothly* was tricky. I had to use `getBoundingClientRect()` to calculate the exact distance between the cursor and the center of the button, and then use GSAP to animate it to a random coordinate within the viewport bounds without it flying off-screen.
*   **Z-Index Wars:** When I built the "Meme Avalanche" feature, the memes kept appearing *behind* my glitch layers or the main text. I had to do a lot of CSS debugging to ensure the meme cards had `z-index: 10001` and the right absolute positioning.
*   **Asset Management:** Originally, I was linking to external meme URLs, but they kept breaking or loading slowly. I solved this by writing Python scripts to download them locally and serve them directly from the `assets` folder.
*   **Performance:** Spawning infinite error notifications and running CSS filters (like SVG noise) at the same time caused some lag. I had to add limits (like capping notifications at 30) and debounce the mousemove events so the browser wouldn't crash.

## Time Taken 
This was basically a weekend project. I'd say I spent about **3 to 4 hours** on it in total. The initial HTML/CSS setup took a few hours, but I spent the bulk of the time tweaking the GSAP animations, fixing the CSS layers, and getting the Python helper scripts to work properly.
