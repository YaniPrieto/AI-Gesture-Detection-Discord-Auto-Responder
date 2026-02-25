# ✋ AI Gesture Detection → Discord Auto-Responder

A real-time computer vision project that detects a **middle finger gesture** from screen capture and automatically sends a screenshot + message to a Discord channel using a webhook.

Built with:
- Python
- OpenCV
- MediaPipe
- MSS (screen capture)
- Discord Webhooks

---

## 📌 Project Overview

This application:

1. Captures the live screen.
2. Uses **MediaPipe Hands** to detect hand landmarks.
3. Identifies a specific gesture (middle finger extended).
4. Captures a screenshot at the moment of detection.
5. Automatically uploads the image to a Discord channel with a custom message.
6. Uses cooldown logic to prevent spam.

This demonstrates real-time computer vision + automation + external service integration.

---

## 🧠 Technical Stack

| Technology | Purpose |
|------------|----------|
| OpenCV | Image processing & rendering |
| MediaPipe | Hand tracking & landmark detection |
| MSS | High-performance screen capture |
| Requests | Discord webhook communication |
| NumPy | Frame processing |

---

## ⚙️ Installation

Install dependencies:

```bash
pip install opencv-python mediapipe mss requests numpy
```

---

## 🔐 Discord Webhook Setup

1. Open Discord
2. Go to your server
3. Edit Channel → Integrations → Webhooks
4. Create New Webhook
5. Copy the Webhook URL
6. Paste it into the script:

```python
WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"
```

---

## ▶️ How It Works

The system checks:

- Middle finger tip is above its PIP joint
- Other fingers are not extended
- If condition is true → trigger event

When triggered:
- Screenshot is saved
- Image is uploaded to Discord
- Random message is attached
- 5-second cooldown prevents spam

---

## 🚀 Run the Project

```bash
python your_script_name.py
```

Press `Q` to exit.

---

## 🛡️ Anti-Spam Protection

The script includes:
- 5-second cooldown between messages
- Temporary file cleanup after upload

This ensures:
- No message flooding
- No storage buildup

---

## 📸 Example Output

When gesture is detected, Discord receives:

- Screenshot attachment
- Random funny message
- Timestamped event

---

## 💡 Use Case Scenarios

- Gesture-triggered automation
- Real-time CV event monitoring
- Discord integration demos
- Fun interactive AI projects
- Proof-of-concept automation systems

---

## 📈 What This Demonstrates

- Real-time computer vision processing
- Landmark-based gesture recognition
- External API integration
- Event-driven automation
- Clean modular Python structure

---

## 👨‍💻 Author

John Prieto  
Game Developer | Computer Vision Enthusiast | Automation Builder

---

## ⚠️ Disclaimer

This project is for educational and demonstration purposes only.  
Ensure webhook URLs remain private.
