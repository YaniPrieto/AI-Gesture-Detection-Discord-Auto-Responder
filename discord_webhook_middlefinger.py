import cv2
import numpy as np
import mediapipe as mp
import mss
import requests
import time
import random
import os

# ==========================
# DISCORD WEBHOOK CONFIG
# ==========================
WEBHOOK_URL = "INSERT DISCORD WEBHOOK URL HERE"

last_sent_time = 0
cooldown_seconds = 10

messages = [
    "Do not let any unwholesome talk come out of your mouths, but only what is helpful for building others up according to their needs, that it may benefit those who listen. - Ephesians 4:29",
    "A gentle answer turns away wrath, but a harsh word stirs up anger. - Proverbs 15:1",
    "Those who consider themselves religious and yet do not keep a tight rein on their tongues deceive themselves, and their religion is worthless. - James 1:26",
    "But I tell you that everyone will have to give account on the day of judgment for every empty word they have spoken. For by your words you will be acquitted, and by your words you will be condemned. - Matthew 12:36-37",
    "But now you must also rid yourselves of all such things as these: anger, rage, malice, slander, and filthy language from your lips. - Colossians 3:8",
]

def send_discord_message_with_image(frame):
    global last_sent_time
    current_time = time.time()

    if current_time - last_sent_time > cooldown_seconds:
        message = random.choice(messages)

        # Save screenshot
        image_path = "middle_finger_capture.jpg"
        cv2.imwrite(image_path, frame)

        try:
            with open(image_path, "rb") as f:
                requests.post(
                    WEBHOOK_URL,
                    data={"content": message},
                    files={"file": f}
                )
            last_sent_time = current_time
        except:
            pass

        # Optional: delete image after upload
        if os.path.exists(image_path):
            os.remove(image_path)


# ==========================
# MEDIAPIPE SETUP
# ==========================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

# ==========================
# SCREEN CAPTURE SETUP
# ==========================
sct = mss.mss()
monitor = sct.monitors[1]

while True:
    screenshot = sct.grab(monitor)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            index_tip = landmarks[8]
            middle_tip = landmarks[12]
            ring_tip = landmarks[16]
            pinky_tip = landmarks[20]

            index_pip = landmarks[6]
            middle_pip = landmarks[10]
            ring_pip = landmarks[14]
            pinky_pip = landmarks[18]

            index_up = index_tip.y < index_pip.y
            middle_up = middle_tip.y < middle_pip.y
            ring_up = ring_tip.y < ring_pip.y
            pinky_up = pinky_tip.y < pinky_pip.y

            if middle_up and not index_up and not ring_up and not pinky_up:
                cv2.putText(
                    frame,
                    "MIDDLE FINGER DETECTED",
                    (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 0, 255),
                    3
                )

                send_discord_message_with_image(frame)

    cv2.imshow("Screen Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()