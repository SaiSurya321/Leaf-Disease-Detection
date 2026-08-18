# 🖱️ Gesture Controlled Virtual Mouse

[![python](https://img.shields.io/badge/python-3.6--3.8.5-blue.svg)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-windows-green.svg)]()
[![license](https://img.shields.io/badge/license-GPL--3.0-orange.svg)](LICENSE)

A touchless interface that lets you control your computer using hand gestures and voice commands — no extra hardware beyond a webcam and microphone. Includes **Proton**, a voice assistant that can launch/stop gesture recognition, search the web, navigate files, and more, alongside real-time gesture-based mouse and system control.

## 📖 Overview

Two things run together in this project:

1. **Gesture control** — MediaPipe tracks hand landmarks from webcam input in real time; a custom binary finger-state encoding classifies the hand shape into a gesture, which is mapped to a mouse/system action via PyAutoGUI, pycaw, and screen_brightness_control.
2. **Voice assistant (Proton)** — listens via microphone (Google Speech Recognition) or a lightweight desktop chat window (built with Eel), responds via text-to-speech, and can trigger gesture recognition, run web searches, navigate files, and handle a few other spoken commands.

An alternate glove-based detection mode (`Gesture_Controller_Gloved.py`) is also included as a drop-in replacement for `Gesture_Controller.py`, for cases where bare-hand tracking is less reliable — it shares the same interface so `Proton.py` can swap between them.

**Currently Windows-only** — system volume control relies on `pycaw`/`comtypes`, which are Windows-specific APIs, and file navigation uses `os.startfile`.

## 🛠️ Features

### Gesture control

| Gesture | Action |
|---|---|
| Open palm | Neutral — no action |
| Two fingers spread (index + middle, "V") | Move cursor |
| Fist | Click-and-drag |
| Three fingers closed together | Left click |
| Index finger only | Right click |
| Index + middle held together | Double click |
| Pinch (non-dominant hand) | Scroll — horizontal or vertical, based on pinch direction |
| Pinch (dominant hand) | System volume / brightness — based on pinch direction |

Gestures are debounced across several consecutive frames before triggering, to avoid false positives from momentary tracking noise.

### Voice assistant (Proton)

| Say | Does |
|---|---|
| "Proton hello" | Greets you |
| "Proton what is your name" | Introduces itself |
| "Proton date" / "Proton time" | Current date/time |
| "Proton search {query}" | Opens a Google search in your browser |
| "Proton location" | Asks for a place, then opens it in Google Maps |
| "Proton launch gesture recognition" | Starts the gesture control module |
| "Proton stop gesture recognition" | Stops it |
| "Proton copy" / "Proton paste" | Clipboard copy/paste |
| "Proton list files" / "Proton open {n}" / "Proton go back" | Basic file navigation from `C:\` |
| "Proton bye" / "Proton wake up" | Sleep / wake the assistant |
| "Proton exit" | Shuts down gesture recognition and the assistant |

## 📊 Tech Stack

| Category | Library |
|---|---|
| Hand tracking | opencv-python 4.5.3.56, mediapipe 0.8.6.2 |
| Mouse control | pyautogui 0.9.53 |
| System volume | pycaw 20181226, comtypes 1.1.10 |
| System brightness | screen-brightness-control 0.9.0 |
| Speech recognition | SpeechRecognition 3.8.1 |
| Text-to-speech | pyttsx3 2.71 |
| Keyboard control (copy/paste) | pynput 1.7.3 |
| Desktop GUI | eel 0.14.0 |
| Wikipedia lookups | wikipedia 1.4.0 |

## 📁 Project Structure

```
Gesture-Controlled-Virtual-Mouse/
├── src/
│   ├── Proton.py                     # main entry point — voice assistant + gesture control
│   ├── Gesture_Controller.py         # hand-based gesture detection & control (MediaPipe)
│   ├── Gesture_Controller_Gloved.py  # alternate glove-based detection mode
│   ├── app.py                        # Eel-based desktop chat GUI, used by Proton.py
│   └── web/                          # HTML/JS frontend for the GUI [confirm folder name/contents]
├── requirements.txt
├── LICENSE
├── CODE_OF_CONDUCT.md
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 – 3.8.5
- Windows OS
- Webcam + microphone
- [Anaconda](https://www.anaconda.com/products/individual) (recommended, for `PyAudio`/`pywin32`)

### Installation

```bash
git clone https://github.com/SaiSurya321/Gesture-Controlled-Virtual-Mouse.git
cd Gesture-Controlled-Virtual-Mouse
```

```bash
conda create --name gest python=3.8.5
conda activate gest
pip install -r requirements.txt
conda install PyAudio
conda install pywin32
```

### Run

```bash
cd src
python Proton.py
```

Say "**Proton launch gesture recognition**" to start the gesture module, or run gesture control on its own (voice assistant not included) by uncommenting the last two lines of `Gesture_Controller.py`:

```python
gc1 = GestureController()
gc1.start()
```

then:

```bash
python Gesture_Controller.py
```

Press **Enter** while the camera window is focused to exit gesture mode.

## 🖐️ How It Works

1. **Hand detection** — MediaPipe locates up to two hands per frame, returning 21 landmark points each.
2. **Gesture encoding** — each finger's open/closed state is derived from landmark distances and packed into a binary-encoded value (`Gest` enum), so specific finger combinations map directly to specific gestures.
3. **Dominant/non-dominant hand handling** — the detected right hand drives cursor/click actions; the other hand drives pinch-based scroll.
4. **Debouncing** — a gesture must hold for several consecutive frames before it's acted on.
5. **Voice layer** — `Proton.py` runs the chat GUI and speech recognition in parallel threads, parses recognized phrases for keywords, and dispatches to the matching handler — including starting/stopping the gesture module in its own thread.

## 🎥 Demo

The original template's demo GIFs live on a different author's repo — replace this section with your own short screen recording (10–15 sec) of both the gesture control and the voice assistant running.

## 🗺️ Roadmap

- [ ] Cross-platform volume/brightness control (replace pycaw with a cross-platform alternative)
- [ ] Gesture customization / remapping
- [ ] Improve tracking stability in low light
- [ ] Decide fate of `ZORO.py` (remove, or merge into the main assistant)

## 🙏 Credits

Built on the open-source **Gesture Controlled Virtual Mouse** concept and codebase, originally developed by Viral Doshi, Nishiket Bidawat, Ankit Sharma, and Parth Sakariya. See the [original repository](https://github.com/xenon-19/Gesture-Controlled-Virtual-Mouse) for the source project and full contributor list.

## 📄 License

Licensed under [GPL-3.0](LICENSE), consistent with the original project this builds on.

## 📬 Contact

Sai Surya Vadde — [LinkedIn](https://www.linkedin.com/in/saisuryavadde116) · [vss.lpu6@gmail.com](mailto:vss.lpu6@gmail.com)
