from cvzone.HandTrackingModule import HandDetector
import threading
import cv2
from PIL import Image
import google.generativeai as ai
import time

# Configure Gemini API key
ai.configure(api_key="AIzaSyBTZNzVd1IIA-qADX1IIPIvFc54qHqofJ0")
model = ai.GenerativeModel("gemini-1.5-flash")  # Use Gemini model

# Initialize webcam
cam = cv2.VideoCapture(0)

# Initialize hand detector
detector = HandDetector(maxHands=2, minTrackCon=0.5)

# Function to show live camera feed with hand landmarks
def feed():
    while True:
        success, img = cam.read()
        hands, img = detector.findHands(img, draw=False)
        cv2.imshow("Live Feed", img)
        key = cv2.waitKey(1)

        # Press 'q' to quit
        if key == ord('q'):
            break

# Function to detect left-hand gesture and capture image
def picture():
    while True:
        success, img = cam.read()
        hands, img = detector.findHands(img, draw=False)

        if hands and len(hands) == 2:
            # Loop through detected hands to find the LEFT hand
            for hand in hands:
                if hand["type"] == "Left":
                    fingers_up = detector.fingersUp(hand)

                    # Check for ✌️ gesture (index and middle fingers up only)
                    if fingers_up == [0, 1, 1, 0, 0]:
                        print("👈 Left-hand gesture detected: Taking picture...")

                        filename = "pictures.jpg"
                        cv2.imwrite(filename, img)

                        img_ans = Image.open(filename)
                        response = model.generate_content(
                            [img_ans, "describe the object that is in my hand"]
                        )

                        print("🤖 Gemini says:", response.text)
                        time.sleep(3)  # Avoid repeated triggering
                        break  # Prevent checking other hands in the same loop

# Run feed and picture functions in separate threads
feed_thread = threading.Thread(target=feed)
picture_thread = threading.Thread(target=picture)

feed_thread.start()
picture_thread.start()
