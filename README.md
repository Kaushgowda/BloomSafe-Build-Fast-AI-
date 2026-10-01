# AI Performance Coach (universal edition)

Works with **no API key at all**. The optional AI coach can be Gemini, Claude, any OpenAI-compatible service, or a free local model (Ollama).

## Run it
1. `python3 server.py` (needs Python 3.8+, nothing to install)
2. Open http://localhost:8000 in Chrome or Edge and tap once to turn on voice.

## What works offline (no key, nothing leaves your computer)
- Interview (from your resume), viva, negotiation, speech and demo modes, with Pressure Mode curveballs
- Live pace, filler and hedge meters, pause tracking, timer and target length
- Resume reading from DOCX, DOC, TXT, pasted text and most text PDFs, with questions built from your own projects and skills
- A rule-based content check: hook, signposting, closing, evidence, ownership ("I" vs "we"), and your most repeated idea
- Camera: self-view, lighting and movement checks on your device
- Scored reports with specific drills

## What the optional AI adds
Adaptive follow-up questions that react to what you said, a written review of structure and content, eye-contact and posture feedback from camera snapshots, screen-aware demo review, and reading scanned or oddly-encoded PDFs (Gemini and Claude only).

Copy `.env.example` to `.env` and uncomment ONE option. Free and private: install Ollama, run `ollama pull llama3.2`, and set `LLM_PROVIDER=ollama`. Local text models ignore camera and screen images, so those reviews need Gemini, Claude or a vision-capable model.

---
# AI Performance Coach

A browser-based AI practice coach for interviews, vivas, speeches, negotiations, and project demos.

## Tech stack

- Frontend: HTML, CSS, JavaScript
- Voice input: Web Speech API
- Voice output: Browser Speech Synthesis API
- Screen sharing: Screen Capture API (`getDisplayMedia`)
- Backend: Python standard library HTTP server
- AI: Google Gemini API
- Resume processing: Python PDF/Word handling + Gemini for PDF/legacy Word cleanup

## Run locally

1. Install Python 3.9 or newer.
2. Copy `.env.example` to a file named `.env`.
3. Create a Gemini API key in Google AI Studio and put it in `.env`:

   `GEMINI_API_KEY=your-real-key`

4. Open a terminal in this folder and run:

   `python server.py`

   On systems where `python` maps to another interpreter, use `python3 server.py`.

5. Open Chrome or Microsoft Edge and visit:

   `http://localhost:8000`

The browser handles microphone speech recognition, speech synthesis, and screen sharing. Gemini is called only by the Python backend, so the API key is not exposed in the frontend.

## Gemini model

The default model is `gemini-3.8-flash`. You can override it in `.env` with `COACH_MODEL=...` if needed.

## API key safety

Never commit or share `.env`. Keep the Gemini API key private.

## Camera
Turn on 📷 Camera (button, or say "camera on" / "camera off" from the menu). It works in every mode. Your browser asks for permission once.
- On your device: a mirrored self-view, live lighting feedback, a rough movement level while you speak, and (in browsers that support face detection) how often you stayed in frame.
- With the Gemini key: a snapshot every 15 seconds while you speak (up to 6) is sent with what you were saying, and the review comments on eye contact, posture, framing, expression and gestures. Snapshots are not stored and are sent only when the report is built.
- The local movement and framing numbers are rough estimates, not measurements. Turn the camera off any time.
