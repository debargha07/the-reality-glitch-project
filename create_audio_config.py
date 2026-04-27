import base64
import os

filepath = r"C:\Users\DEBARGHA\Downloads\Fahhh - QuickSounds.com.mp3.mpeg"
with open(filepath, "rb") as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

js_content = f"""// AUDIO CONFIGURATION
const DODGE_SOUND_B64 = "data:audio/mpeg;base64,{b64}";

const AudioContext = window.AudioContext || window.webkitAudioContext;
let actx = null;
let masterGain = null;
let audioUnlocked = false;
let lastSoundTime = 0;

function unlockAudio() {{
    if (audioUnlocked) return;
    const silent = new Audio();
    silent.play().catch(() => {{}});
    audioUnlocked = true;
}}

document.addEventListener('mousemove', unlockAudio, {{ once: true }});
document.addEventListener('touchstart', unlockAudio, {{ once: true }});

async function playDodgeSound(rate = null, vol = 0.65, force = false) {{
    if (!audioUnlocked) return;
    
    const now = Date.now();
    if (!force && now - lastSoundTime < 280) return;
    lastSoundTime = now;

    if (!actx) {{
        actx = new AudioContext();
        masterGain = actx.createGain();
        masterGain.connect(actx.destination);
    }}

    try {{
        const resp = await fetch(DODGE_SOUND_B64);
        const buf = await resp.arrayBuffer();
        const decoded = await actx.decodeAudioData(buf);

        const source = actx.createBufferSource();
        source.buffer = decoded;
        source.playbackRate.value = rate !== null ? rate : (0.85 + Math.random() * 0.35);

        const gain = actx.createGain();
        gain.gain.value = vol;

        source.connect(gain);
        gain.connect(masterGain);
        source.start(0);
    }} catch(e) {{}}
}}

function triggerAudioDuck() {{
    if (actx && masterGain) {{
        masterGain.gain.cancelScheduledValues(actx.currentTime);
        masterGain.gain.setValueAtTime(0.3, actx.currentTime);
        masterGain.gain.linearRampToValueAtTime(1.0, actx.currentTime + 1.5);
    }}
}}
"""

with open(r"C:\Users\DEBARGHA\OneDrive\Desktop\p1\audio.config.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Created audio.config.js")
